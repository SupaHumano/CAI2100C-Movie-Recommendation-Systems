#!/usr/bin/env python3
"""Produce a single-file Assignment 8 notebook with verified authentic research subsets.
This builder *only* labels data authentic after exact original IMDb full-file SHA-256 checks.
No data is synthesized in the authentic build.
"""
from pathlib import Path
from zipfile import ZipFile
import sys, io, os, gzip, json, hashlib, base64, tempfile
import pandas as pd
import nbformat
from nbclient import NotebookClient

IMDB_FULL_SHA={
 'IMDb movies.csv':'0a106f5bd8de699cd092b0e02e6968ffb4ecde8b1c13b1ec899c3eb6873e8122',
 'IMDb ratings.csv':'92a29e0eb24fdd7f8977378e08aa59de5f3bab2433c6eef508af85e59a222675'}
IMDB_COLS=['imdb_title_id','title','genre','description','director','actors','votes','avg_vote']
COHORT_PAIRS=[('females_18age_avg_vote','females_18age_votes'),('females_30age_avg_vote','females_30age_votes'),('females_45age_avg_vote','females_45age_votes'),('males_18age_avg_vote','males_18age_votes'),('males_30age_avg_vote','males_30age_votes'),('males_45age_avg_vote','males_45age_votes')]
COHORT_COLS=[x for p in COHORT_PAIRS for x in p]
SOURCE={
  'IMDb movies.csv': 'https://raw.githubusercontent.com/Abkas/Machine-Learning-Approaches-for-Movie-Rating-Prediction-on-IMDb-Dataset/509c026e32a6fa78cfc987a0aa39f47cc47fd243/Dataset/IMDb%20movies.csv',
  'IMDb ratings.csv':'https://raw.githubusercontent.com/Abkas/Machine-Learning-Approaches-for-Movie-Rating-Prediction-on-IMDb-Dataset/509c026e32a6fa78cfc987a0aa39f47cc47fd243/Dataset/IMDb%20ratings.csv',
  'movies_metadata.csv':'https://raw.githubusercontent.com/nmsohn/kaggle-movie/751ce2616c0aa7667b93277c37365b0c4edbc929/movies_metadata.csv',
  'links_small.csv':'https://raw.githubusercontent.com/nmsohn/kaggle-movie/751ce2616c0aa7667b93277c37365b0c4edbc929/links_small.csv',
  'ratings_small.csv':'https://raw.githubusercontent.com/nmsohn/kaggle-movie/751ce2616c0aa7667b93277c37365b0c4edbc929/ratings_small.csv',
}
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def produce(raw_dir:Path, template:Path, output:Path, provenance_required=True):
    raw_dir=Path(raw_dir); output=Path(output)
    if provenance_required:
        for fn,expected in IMDB_FULL_SHA.items():
            path=raw_dir/fn
            assert path.exists(),f'Authentic source file not downloaded: {fn}'
            actual=sha(path)
            assert actual==expected,f'Original IMDb file did not match pinned SHA256: {fn}, {actual} != {expected}'
    # Snapshot IMDb: identical deterministic filter as original notebook, reduced to used columns.
    movies=pd.read_csv(raw_dir/'IMDb movies.csv',low_memory=False)
    ratings=pd.read_csv(raw_dir/'IMDb ratings.csv',low_memory=False)
    assert set(IMDB_COLS).issubset(movies.columns)
    assert set(['imdb_title_id',*COHORT_COLS]).issubset(ratings.columns)
    movies['votes']=pd.to_numeric(movies['votes'],errors='coerce').fillna(0)
    movies=movies.loc[movies.votes.ge(1000)&movies.title.notna()&movies.imdb_title_id.notna()]
    movies=movies.sort_values(['votes','imdb_title_id'],ascending=[False,True]).drop_duplicates('imdb_title_id').head(3000)
    assert len(movies)>=40,(len(movies),'not enough real IMDb eligible movies')
    movies=movies[IMDB_COLS]
    ratings=ratings[['imdb_title_id',*COHORT_COLS]].drop_duplicates('imdb_title_id')
    ratings=ratings.loc[ratings.imdb_title_id.isin(movies.imdb_title_id)]
    assert len(ratings)>=40
    # Snapshot classroom source: keep the complete small ratings and links files; only metadata subset needed for the models.
    meta=pd.read_csv(raw_dir/'movies_metadata.csv',low_memory=False)
    links=pd.read_csv(raw_dir/'links_small.csv',low_memory=False)
    small=pd.read_csv(raw_dir/'ratings_small.csv',low_memory=False)
    assert {'id','title','overview'}.issubset(meta.columns)
    assert {'movieId','tmdbId'}.issubset(links.columns)
    assert {'userId','movieId','rating'}.issubset(small.columns)
    meta['numeric_id']=pd.to_numeric(meta['id'],errors='coerce')
    links['numeric_id']=pd.to_numeric(links['tmdbId'],errors='coerce')
    valid=set(links.numeric_id.dropna().astype('int64'))
    meta=meta.loc[meta.numeric_id.isin(valid)].drop(columns=['numeric_id'])
    # Column set preserves tags etc used in the classroom content section.
    meta=meta[['id','title','overview','tagline']]
    assert len(meta)>=30 and len(small)>=200,(len(meta),len(small))
    snapshots={'IMDb movies.csv':movies,'IMDb ratings.csv':ratings,
      'movies_metadata.csv':meta,'links_small.csv':links.drop(columns=['numeric_id']),
      'ratings_small.csv':small}
    compressed={};metadata={}
    for filename, frame in snapshots.items():
        bb=frame.to_csv(index=False).encode('utf-8')
        packed=gzip.compress(bb,compresslevel=9,mtime=0)
        compressed[filename]=base64.b64encode(packed).decode('ascii')
        metadata[filename]={'rows':len(frame),'size_csv':len(bb),'size_gzip':len(packed),'snapshot_sha256':hashlib.sha256(bb).hexdigest(),'original_source_url':SOURCE[filename]}
    nb=nbformat.read(template,as_version=4)
    assert len([c for c in nb.cells if c.cell_type=='code'])==12
    embedded_code='''# My original-data research snapshots are embedded inside this notebook.\n# No internet, authentication, file uploads or Kaggle access are required.\nfrom pathlib import Path as _EmbeddedPath\nimport base64 as _embedded_b64, gzip as _embedded_gzip, hashlib as _embedded_hashlib, tempfile as _embedded_tempfile\n_EMBEDDED_FILES = '''+repr(compressed)+'''\n_EMBEDDED_META = '''+repr(metadata)+'''\n_EMBEDDED_DIR = _EmbeddedPath(_embedded_tempfile.mkdtemp(prefix='a8_verified_'))\nfor _filename,_payload in _EMBEDDED_FILES.items():\n    _raw = _embedded_gzip.decompress(_embedded_b64.b64decode(_payload))\n    _fingerprint = _embedded_hashlib.sha256(_raw).hexdigest()\n    assert _fingerprint == _EMBEDDED_META[_filename]['snapshot_sha256'], 'Embedded academic data failed integrity verification: ' + _filename\n    (_EMBEDDED_DIR/_filename).write_bytes(_raw)\nprint('I verified 5 embedded academic research snapshots:', {k: v['rows'] for k,v in _EMBEDDED_META.items()})\n'''
    nb.cells.insert(2,nbformat.v4.new_code_cell(embedded_code))
    # Keep original loader but force embedded paths first to eliminate network calls and avoid changing downstream research mathematics.
    original_code=nb.cells[3].source
    anchor="DATA_PATHS, DATA_ORIGINS, DATA_ERRORS = {}, {}, {}"
    assert anchor in original_code
    original_code=original_code.replace(anchor,anchor+"\nDATA_PATHS.update({name: _EMBEDDED_DIR/name for name in _EMBEDDED_FILES})\nDATA_ORIGINS.update({name: 'Pinned offline research snapshot (verified SHA-256): '+str(_EMBEDDED_DIR/name) for name in _EMBEDDED_FILES})")
    original_code=original_code.replace("'IMDb movies.csv':'0a106f5bd8de699cd092b0e02e6968ffb4ecde8b1c13b1ec899c3eb6873e8122'", "'IMDb movies.csv':_EMBEDDED_META['IMDb movies.csv']['snapshot_sha256']")
    original_code=original_code.replace("'IMDb ratings.csv':'92a29e0eb24fdd7f8977378e08aa59de5f3bab2433c6eef508af85e59a222675'", "'IMDb ratings.csv':_EMBEDDED_META['IMDb ratings.csv']['snapshot_sha256']")
    nb.cells[3].source=original_code
    # Avoid claiming the full original Kaggle CSVs were included.
    intro=nb.cells[0].source
    intro=intro.replace('I use the assigned IMDb Extensive dataset', 'I use verified, included research snapshots derived from the assigned IMDb Extensive dataset')
    nb.cells[0].source=intro
    nb.cells[1].source='''## My single-file, reproducible research submission\n\nI prepared one offline notebook containing **five compressed, integrity-checked snapshots of authentic source CSVs**. It runs with **Runtime → Run all**, without external files, passwords, manual uploads or network access.\n\n- **Required IMDb assignments:** my snapshot includes the 3,000 high-vote movies analyzed by my code and corresponding IMDb cohort-average ratings.\n- **MovieLens/TMDB extension:** my snapshot includes the small MovieLens rating and link tables and metadata restricted to linked films.\n- The embedded subsets **are not** the complete 85,855-record IMDb dataset or the teacher's large original ZIP. I identify each source and full original-file fingerprints in the provenance cell; I do not mislabel or inflate row counts.\n- I reproduce content-based recommendations and held-out cohort/user-based collaborative evaluations with the same input snapshots used to generate the saved outputs.\n\n**Sources and academic attribution:** [Stefano Leone's IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset), pinned [IMDb dataset mirror](https://github.com/Abkas/Machine-Learning-Approaches-for-Movie-Rating-Prediction-on-IMDb-Dataset/tree/509c026e32a6fa78cfc987a0aa39f47cc47fd243/Dataset), and [Rounak Banik's MovieLens/TMDB collection](https://www.kaggle.com/rounakbanik/the-movies-dataset). Embedded data are for educational research; I do not claim to redistribute the full original sources.\n'''
    for i,c in enumerate(nb.cells):
        if c.cell_type=='markdown':
            c.source=c.source.replace('I use the two assigned Kaggle files, `IMDb movies.csv` and `IMDb ratings.csv`. I first validate my inputs and document their exact SHA-256 checksums and row counts.', 'I use two **embedded research-subset** CSV snapshots derived from the assigned IMDb Extensive Kaggle files and validate their SHA-256 checksums and row counts.')
            c.source=c.source.replace('I use the teacher-provided ZIP **when it is present**. Otherwise I automatically retrieve', 'I use authentic embedded snapshots of the public MovieLens/TMDB dataset; my original classroom source is separate. I can also retrieve')
    # New scientific provenance at top, not from synthetic fixtures.
    prov=nbformat.v4.new_markdown_cell('## Embedded research snapshots — integrity and scope\n\n'+
        '\n'.join(f'- **{name}**: {meta["rows"]:,} rows · SHA-256 `{meta["snapshot_sha256"]}` · [source]({meta["original_source_url"]})' for name,meta in metadata.items())+
        '\n\n**Full original IMDb CSV hashes (pre-subsetting):** '+', '.join(f'`{fn}` = `{h}`' for fn,h in IMDB_FULL_SHA.items())+
        '\n\nMovieLens snapshots originate from a separate, pinned public source. I do not identify them as byte-identical to the instructor’s ZIP. The large full MovieLens `ratings.csv` is **not** embedded, since the classroom model uses `ratings_small.csv`.')
    nb.cells.insert(2,prov)
    nb.metadata.setdefault('a8_provenance',{})
    nb.metadata['a8_provenance'].update({'student':'Juan Luna Santibanez','source_type':'Authentic pinned Kaggle-data mirror research subsets' if provenance_required else 'SYNTHETIC TEST FIXTURES — NEVER SUBMIT','original_imdb_sha256':IMDB_FULL_SHA if provenance_required else 'unverified','file_snapshots':metadata})
    for c in nb.cells:
        if c.cell_type=='code':c.execution_count=None;c.outputs=[]
    nbformat.validate(nb)
    output.parent.mkdir(parents=True,exist_ok=True)
    nbformat.write(nb,output)
    print('WROTE',output,'bytes',output.stat().st_size,'source rows',{k:v['rows'] for k,v in metadata.items()},flush=True)
    return output

if __name__=='__main__':
    # Arguments: raw_data_dir, template.ipynb, output.ipynb, AUTHENTIC or SYNTHETIC_TEST
    src=Path(sys.argv[1]);tp=Path(sys.argv[2]);out=Path(sys.argv[3]);auth=sys.argv[4]=='AUTHENTIC'
    if src.joinpath('Assignment 8-machinelearning.zip').exists() and not src.joinpath('movies_metadata.csv').exists():
        with ZipFile(src/'Assignment 8-machinelearning.zip') as z:
            for name in ('movies_metadata.csv','links_small.csv','ratings_small.csv'):
                found=[x for x in z.namelist() if Path(x).name==name and '__MACOSX' not in x]
                assert len(found)==1,(name,found)
                (src/name).write_bytes(z.read(found[0]))
    produce(src,tp,out,auth)