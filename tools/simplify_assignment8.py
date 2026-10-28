"""Build one portable two-task IMDb notebook from the previously validated research subset.
Does not access a network, store any checksums, or encode datasets in Base64.
"""
import ast
import base64
import gzip
import json
import sys
from pathlib import Path
import nbformat

SOURCE = Path(sys.argv[1])
DEST = Path(sys.argv[2])
old = nbformat.read(SOURCE, as_version=4)

# Read the existing source-data snapshot without executing any notebook code.
large = next(c for c in old.cells if c.cell_type == 'code' and '_EMBEDDED_FILES = ' in c.source)
assign = next(n for n in ast.parse(large.source).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='_EMBEDDED_FILES' for t in n.targets))
snapshots = ast.literal_eval(assign.value)
movies_csv = gzip.decompress(base64.b64decode(snapshots['IMDb movies.csv'])).decode('utf-8')
ratings_csv = gzip.decompress(base64.b64decode(snapshots['IMDb ratings.csv'])).decode('utf-8')
assert "'''" not in movies_csv and "'''" not in ratings_csv
assert movies_csv.count('\n')==3001 and ratings_csv.count('\n')==3001

# A plain-text CSV block is the entire data layer. No download, compression, Base64, hashes or filesystem.
imports = '''from io import StringIO
import platform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

np.random.seed(42)
print('Python:', platform.python_version(), '| Pandas:', pd.__version__)

def recommend_by_content(frame, matrix, selected_title, k=10):
    found = np.flatnonzero(frame.title.astype(str).str.casefold().eq(selected_title.casefold()))
    if not len(found):
        raise ValueError('Title not found: '+selected_title)
    target = int(found[0])
    similarity = linear_kernel(matrix[target],matrix).ravel()
    indices = np.argsort(-similarity,kind='stable')
    indices = indices[indices!=target][:k]
    result = frame.iloc[indices][['title']].copy()
    result['cosine_similarity']=similarity[indices]
    return result.reset_index(drop=True)
'''
data = '''# @title Data — IMDb CSV records included in this notebook { display-mode: "form" }
# @markdown 3,000 genuine movies and matching audience-cohort ratings. No downloads.
# The CSV records below are plain text, not an encoded payload.
_IMDB_MOVIES_CSV = '''+"'''"+movies_csv+"'''"+'''
_IMDB_RATINGS_CSV = '''+"'''"+ratings_csv+"'''"+'''
imdb_movies_raw = pd.read_csv(StringIO(_IMDB_MOVIES_CSV), low_memory=False)
imdb_ratings_raw = pd.read_csv(StringIO(_IMDB_RATINGS_CSV), low_memory=False)
del _IMDB_MOVIES_CSV, _IMDB_RATINGS_CSV
assert len(imdb_movies_raw)==3000 and len(imdb_ratings_raw)==3000
assert imdb_movies_raw.imdb_title_id.is_unique and imdb_ratings_raw.imdb_title_id.is_unique
print('Loaded IMDb records:', len(imdb_movies_raw),'films and',len(imdb_ratings_raw),'cohort rating rows')
'''
# Validate that each dataset is there and ready for the exact assigned algorithms.
cohorts = '''COHORTS = {
 'Women 18–29': ('females_18age_avg_vote', 'females_18age_votes'),
 'Women 30–44': ('females_30age_avg_vote', 'females_30age_votes'),
 'Women 45+': ('females_45age_avg_vote', 'females_45age_votes'),
 'Men 18–29': ('males_18age_avg_vote', 'males_18age_votes'),
 'Men 30–44': ('males_30age_avg_vote', 'males_30age_votes'),
 'Men 45+': ('males_45age_avg_vote', 'males_45age_votes')}
cohort_cols = [c for pair in COHORTS.values() for c in pair]
assert {'imdb_title_id','title','genre','description','director','actors','votes','avg_vote'}.issubset(imdb_movies_raw.columns)
assert {'imdb_title_id', *cohort_cols}.issubset(imdb_ratings_raw.columns)
'''

cells=[]
def md(txt):cells.append(nbformat.v4.new_markdown_cell(txt.strip()+'\n'))
def code(txt,fold=False):
    c=nbformat.v4.new_code_cell(txt.rstrip()+'\n')
    if fold:
        c.metadata['cellView']='form'
        c.metadata['jupyter']={'source_hidden':True,'outputs_hidden':False}
        c.metadata['colab']={}
    cells.append(c)

md('''# Assignment 8 — Movie Recommendation Systems

**Juan Luna Santibanez**  
**Miami Dade College | CAI2100C — Machine Learning Foundations**  
**Professor Beth Muturi**

## My assignment

I completed the **two tasks** in my instructor's Assignment 8:

1. **Task 1 — Content-Based Filtering:** I use movie metadata, TF-IDF and cosine similarity.
2. **Task 2 — Collaborative Filtering approximation:** I analyze the patterns of IMDb's aggregated ratings across six audience groups.

I designed this as **one Jupyter notebook** that runs in Google Colab, Kaggle Code or local Jupyter with ordinary scientific Python libraries. The data required for both tasks are already included as **readable CSV text** in one collapsed cell. I do not need to download files, set a path, enter credentials, or use external datasets.

**Data scope:** I use a reproducible research sample of **3,000 authentic IMDb films** and their **3,000 matching cohort-rating records**, selected from the public IMDb Extensive collection. This is not an analysis of all IMDb titles.

[IMDb Extensive — Stefano Leone](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset) · [Project GitHub](https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems) · [Instructor reference — Rounak Banik](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems)
''')
md('''## How I organized my notebook

I keep source data, methodology and results separate. I placed the two real CSV research samples into a single folded cell as **plain text**, so they remain readable when expanded. I use `StringIO` to load them directly into Pandas. I do not need hashes, Base64 strings, compressed data, installers or extra ZIP files.

**To reproduce my results:** Open this `.ipynb`, choose **Run all**, and read the tables, graphs, MAE/RMSE metrics and conclusions. I save the results in the notebook itself.
''')
code(imports)
md('''## Data — two IMDb CSV research samples

I selected up to 3,000 movies with at least 1,000 overall votes and joined their original IMDb IDs with the available demographic-rating rows. I retain genre, description, director, actors, votes, average rating and six age/gender cohort ratings. **These records are real but selected; the sample does not represent every title in the original source.**

The next cell contains the actual CSV rows, not encoded or synthetic values. I leave it collapsed in notebook interfaces so I can focus on the two assignments. Expanding the cell reveals ordinary CSV lines.
''')
code(data,fold=True)
md('''## Task 1 — Content-Based Filtering

I represent each movie using its **genre, director, actors and description**. TF-IDF converts the text into numerical word features; I compare those feature vectors with **cosine similarity** and recommend other movies with related text. I exclude the original query title.

A high similarity value describes metadata resemblance. It does **not** guarantee that a person will like both films.
''')
code(cohorts+ '\n'+old.cells[9].source)
code(old.cells[11].source)
md('''## Task 2 — Collaborative Filtering approximation

The IMDb Extensive ratings file contains **aggregated audience statistics**, not `userId`–`movieId`–`rating` interactions. I therefore compare six demographic audience groups instead of claiming personalized recommendations.

I represent their film-average ratings in a group-by-movie matrix, require at least **30 votes** for a group/movie observation, and calculate **Pearson correlations** for groups with enough common movies. I estimate a group's missing average rating from positively correlated groups.

For evaluation, I hide approximately **15% of eligible observed group averages**, compute predictions from training observations only, and report **MAE**, **RMSE** and a simple training-group-mean baseline. The scores describe group-average errors on IMDb's 1–10 scale, not individuals' preferences.
''')
code(old.cells[13].source)
code(old.cells[14].source)
md('''## My results and interpretation

I compare the two **required IMDb methods**, not different rating scales or unrelated datasets. Content-Based Filtering yields a ranked list of similar movies, whereas the cohort-correlation approach produces estimated **group-level averages**. These methods answer different questions, so I do not compare their cosine similarity values with MAE/RMSE as if they were identical measurements.
''')
code('''summary = pd.DataFrame([
 {'Task':'1 — Content-Based', 'Data':'Movie descriptions and metadata', 'Result':f'{len(imdb_content)} recommended films', 'Measurement':'TF-IDF cosine similarity'},
 {'Task':'2 — Cohort rating patterns', 'Data':'Six demographic rating groups', 'Result':f'{imdb_scores["Held-out group means"]} held-out group means', 'Measurement':f'MAE {imdb_scores["MAE"]:.4f}; RMSE {imdb_scores["RMSE"]:.4f}; baseline MAE {imdb_scores["Training-group-mean baseline MAE"]:.4f}'}
])
display(summary)
print('PASS — Both assigned IMDb recommendation methods completed from embedded real source records.')
''')
md('''## My conclusion

I found that the **Content-Based** method recommends movies based on information describing their content. My second approach studies IMDb's **demographic rating patterns** using correlations between cohort averages; because it does not contain individual user histories, it cannot predict a particular viewer's preferences in the way that user-based collaborative filtering or SVD can.

**Limitations:** I used 3,000 selected IMDb titles rather than the entire original collection; popular titles are overrepresented. Cohort averages are aggregated statistics, not personal ratings. I reported held-out evaluation with a training-only baseline and documented the scope of each result.

**Sources:** [Stefano Leone, IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset); Professor Beth Muturi's Assignment 8 notebook; [Rounak Banik, Movie Recommender Systems](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems); [scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
''')

new=nbformat.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'},'colab':{'toc_visible':True},'author':'Juan Luna Santibanez','assignment':'CAI2100C — Assignment 8','data_scope':'IMDb Extensive 3000 authentic selected movies and cohort records; no MovieLens extension in this two-task version'})
nbformat.validate(new)
DEST.parent.mkdir(parents=True,exist_ok=True)
nbformat.write(new,DEST)
print('BUILT',DEST,'bytes',DEST.stat().st_size,'cells',len(new.cells),'codes',sum(c.cell_type=='code' for c in new.cells))