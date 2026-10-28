# My scientific methodology — Assignment 8

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

## Research question
I compare content-feature similarity against two distinct sources of rating patterns: IMDb Extensive **cohort averages** and MovieLens **individual user events**. My instructor explicitly assigned two IMDb methods; I independently label the MovieLens example as a classroom extension.

## Source integrity and snapshot construction
I downloaded five CSV files from original public collections pinned to fixed GitHub commits. Before selecting the IMDb sample, I verified the **entire original 47,840,433-byte `IMDb movies.csv`** and **17,363,252-byte `IMDb ratings.csv`** against the expected SHA-256 fingerprints in [OFFLINE_PROVENANCE.json](OFFLINE_PROVENANCE.json).

I selected up to **3,000** IMDb movies with at least 1,000 overall votes, sorted by vote count and IMDb title identifier. I joined those identifiers to the six cohort-average and cohort-vote-count columns. I saved **exactly 3,000** genuine movie rows and matching cohort-rating rows. This reproduces the original notebook's declared **research sample**, not its complete 85,855-record raw database.

For MovieLens/TMDB, I used a pinned public-source subset: **9,099** linked movie metadata records (title, overview and tagline), **9,125** ID mappings, and the full **100,004** rating events from `ratings_small.csv`. I did not include the enormous `ratings.csv`, which is unnecessary for my classroom algorithms, and I did not claim the public mirror is byte-identical to the instructor ZIP.

I serialized each snapshot to CSV, compressed it with deterministic gzip and embedded it as Base64 in one Jupyter notebook. On execution, I verify **each snapshot SHA-256**, extract the files to a temporary directory and run the models. The notebook requires **no external data**, but it uses ordinary Pandas, NumPy, SciPy, Matplotlib and scikit-learn packages.

## My Task 1 — IMDb Content-Based
I combine genre, director, actors and description into textual features. `TfidfVectorizer` constructs a sparse unigram/bigram matrix with up to 6,000 features. I rank other movies against a chosen title using cosine similarity, excluding the selected title from recommendations.

## My Task 2 — IMDb Collaborative cohort approximation
I build a 6×N matrix using gender/age cohort mean ratings where each cohort has at least 30 votes for a title. I calculate Pearson correlation on co-observed film ratings, requiring adequate overlap. I hold out ~15% of usable matrix cells subject to preserving training support and estimate those missing **group averages** from positively correlated neighboring cohorts. I evaluate held-out **MAE and RMSE** against a training-group-mean baseline on the 1–10 IMDb scale.

**Limitations:** this is not personalized user-item collaborative filtering, and no single-viewer identification can be inferred from the cohort averages.

## My MovieLens/TMDB classroom extension
I match MovieLens links to TMDB film metadata, construct a description-based TF-IDF vectorizer and calculate cosine similarity. I separately split `ratings_small.csv` into deterministic 80/20 train/test records, center user ratings by training-user means, calculate user-user cosine similarities, and estimate held-out movie ratings from up to 25 positively similar neighbors. I evaluate MAE, RMSE, prediction coverage and a matched training-user-mean baseline on the 0.5–5 rating scale.

**Limitations:** this neighborhood model is not the class example's Surprise/SVD; MovieLens errors and IMDb cohort-average errors should not be compared on raw magnitude.

## My verification gate
A GitHub build runner downloaded pinned authentic sources, checked the full IMDb SHA-256 values, generated the embedded notebook, and ran it from a clean temporary working directory without source data files. **All 13 code cells succeeded and their outputs were saved**. This verifies a single-file, offline-data workflow. The notebook's model results refer only to the genuine **documented research snapshots**.

See [OFFLINE_PROVENANCE.json](OFFLINE_PROVENANCE.json) for row counts, source references and per-snapshot SHA-256 checksums.

## Sources
- Beth Muturi, Assignment 8 classroom notebook and follow-up course email, CAI2100C.
- [IMDb Extensive by Stefano Leone](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Pinned IMDb data mirror](https://github.com/Abkas/Machine-Learning-Approaches-for-Movie-Rating-Prediction-on-IMDb-Dataset/tree/509c026e32a6fa78cfc987a0aa39f47cc47fd243/Dataset).
- [The Movies Dataset by Rounak Banik](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).
- [scikit-learn recommendation/vectorization methods](https://scikit-learn.org/stable/modules/feature_extraction.html).
