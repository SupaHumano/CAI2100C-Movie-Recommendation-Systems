"""Movie recommendations for IMDb Extensive. Demographic averages are not personal ratings."""
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
COHORTS={"Women 18-29":("females_18age_avg_vote","females_18age_votes"),"Women 30-44":("females_30age_avg_vote","females_30age_votes"),"Women 45+":("females_45age_avg_vote","females_45age_votes"),"Men 18-29":("males_18age_avg_vote","males_18age_votes"),"Men 30-44":("males_30age_avg_vote","males_30age_votes"),"Men 45+":("males_45age_avg_vote","males_45age_votes")}
def find_data(roots=(".",)):
    paths={}
    for name in ("IMDb movies.csv","IMDb ratings.csv"):
        found=[]
        for root in map(Path,roots):
            found.append(root/name)
            if root.is_dir():found.extend(root.glob("**/"+name))
        paths[name]=next((p for p in found if p.is_file()),None)
    if any(p is None for p in paths.values()):
        raise FileNotFoundError("Download IMDb movies.csv and IMDb ratings.csv from https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset")
    return paths
def load_imdb(paths,limit=3000,min_votes=1000):
    m=pd.read_csv(paths["IMDb movies.csv"],low_memory=False)
    r=pd.read_csv(paths["IMDb ratings.csv"],low_memory=False)
    required={"imdb_title_id","title","genre","description","director","actors","votes","avg_vote"}
    ratings_required={"imdb_title_id"}|{x for pair in COHORTS.values() for x in pair}
    if required-set(m):raise ValueError("IMDb movie columns missing: "+str(required-set(m)))
    if ratings_required-set(r):raise ValueError("IMDb rating columns missing: "+str(ratings_required-set(r)))
    m["votes"]=pd.to_numeric(m.votes,errors="coerce").fillna(0)
    m["avg_vote"]=pd.to_numeric(m.avg_vote,errors="coerce")
    m=m[m.votes.ge(min_votes)&m.title.notna()&m.imdb_title_id.notna()]
    m=m.sort_values("votes",ascending=False).drop_duplicates("imdb_title_id").head(limit).copy()
    for k in ("title","genre","description","director","actors"):m[k]=m[k].fillna("").astype(str)
    out=m.merge(r[["imdb_title_id"]+[x for pair in COHORTS.values() for x in pair]].drop_duplicates("imdb_title_id"),on="imdb_title_id",how="left",validate="one_to_one")
    if len(out)<5:raise ValueError("At least five IMDb movies are required after filtering")
    return out.reset_index(drop=True)
def content_features(movies):
    text=movies.genre.str.replace(","," ",regex=False)+" "+movies.director.str.replace(","," ",regex=False)+" "+movies.actors.str.replace(","," ",regex=False)+" "+movies.description
    return TfidfVectorizer(stop_words="english",ngram_range=(1,2),max_features=6000).fit_transform(text)
def content_recommend(movies,features,title,n=10):
    matched=np.flatnonzero(movies.title.str.casefold().eq(title.casefold()))
    if not len(matched):raise KeyError("Unknown selected IMDb title: "+title)
    i=int(matched[0]);sim=(features@features[i].T).toarray().ravel()
    ids=np.argsort(-sim,kind="stable");ids=ids[ids!=i][:n]
    result=movies.iloc[ids][["title","genre","imdb_title_id","avg_vote"]].copy()
    result["similarity"]=sim[ids]
    return result.reset_index(drop=True)
def cohort_matrix(movies,min_votes=30):
    rows=[]
    for mean,count in COHORTS.values():
        v=pd.to_numeric(movies[mean],errors="coerce")
        votes=pd.to_numeric(movies[count],errors="coerce").fillna(0)
        rows.append(v.where(v.between(1,10)&votes.ge(min_votes)).to_numpy(float))
    return pd.DataFrame(rows,index=list(COHORTS),columns=movies.imdb_title_id.tolist())
def cohort_similarity(matrix,min_overlap=15):
    x=matrix.to_numpy(float);n=x.shape[0];out=np.eye(n)
    for i in range(n):
        for j in range(i+1,n):
            mask=np.isfinite(x[i])&np.isfinite(x[j])
            corr=float(np.corrcoef(x[i,mask],x[j,mask])[0,1]) if mask.sum()>=min_overlap and np.std(x[i,mask])>1e-10 and np.std(x[j,mask])>1e-10 else 0.
            out[i,j]=out[j,i]=np.clip(corr,-1,1)
    return pd.DataFrame(out,index=matrix.index,columns=matrix.index)
def cohort_predict(matrix,sim,row,col):
    x=matrix.to_numpy(float);means=np.nanmean(x,axis=1);average=float(np.nanmean(x))
    base=means[row] if np.isfinite(means[row]) else average
    weights=sim.iloc[row].to_numpy(float).copy();weights[row]=0
    use=(weights>0)&np.isfinite(x[:,col])&np.isfinite(means)
    if not use.any():return float(np.clip(base,1,10))
    predicted=base+np.dot(weights[use],x[use,col]-means[use])/weights[use].sum()
    return float(np.clip(predicted,1,10))
def cohort_recommend(movies,matrix,cohort="Women 18-29",n=10):
    if cohort not in matrix.index:raise KeyError(cohort)
    row=list(matrix.index).index(cohort);sim=cohort_similarity(matrix)
    available=[j for j in range(matrix.shape[1]) if pd.isna(matrix.iloc[row,j]) and matrix.iloc[:,j].notna().sum()>=2]
    unseen=bool(available)
    if not unseen:available=[j for j in range(matrix.shape[1]) if matrix.iloc[:,j].notna().sum()>=3]
    if not available:raise ValueError("Not enough cohort averages for predictions")
    estimates=np.array([cohort_predict(matrix,sim,row,j) for j in available])
    order=np.argsort(-estimates)[:n]
    keys=matrix.columns[np.array(available)[order]]
    result=movies.set_index("imdb_title_id").loc[keys,["title","genre","avg_vote"]].copy()
    result["estimated_cohort_average"]=estimates[order]
    result.attrs["note"]="Missing-cell estimates" if unseen else "Descriptive group averages, not individual preferences"
    return result.reset_index()
def evaluate_cohort(matrix,seed=42,fraction=0.15):
    observed=np.argwhere(np.isfinite(matrix.to_numpy(float)))
    if len(observed)<60:raise ValueError("Not enough cohort observations")
    rng=np.random.default_rng(seed);rng.shuffle(observed)
    train=matrix.copy();actual=[];target=max(1,round(len(observed)*fraction))
    for i,j in observed:
        if len(actual)>=target:break
        if train.iloc[i].notna().sum()<=15 or train.iloc[:,j].notna().sum()<=2:continue
        actual.append((int(i),int(j),float(matrix.iloc[i,j])));train.iloc[i,j]=np.nan
    if not actual:raise ValueError("Could not create validation subset")
    sim=cohort_similarity(train)
    errors=np.array([cohort_predict(train,sim,i,j)-truth for i,j,truth in actual])
    return {"held_out":len(actual),"MAE":float(np.mean(abs(errors))),"RMSE":float(np.sqrt(np.mean(errors**2)))}
