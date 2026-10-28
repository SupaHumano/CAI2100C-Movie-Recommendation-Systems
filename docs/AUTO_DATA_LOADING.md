# My data loading and reproducibility — Assignment 8

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

I use one Jupyter notebook: [Assignment 8 — Juan Luna Santibanez](../notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).

## How I get authentic data automatically

My notebook first locates previously attached files. If needed, I install the official `kagglehub` package and use `kagglehub.dataset_download(dataset_handle, path=filename)` to request individual CSVs:

- IMDb Extensive: `stefanoleone992/imdb-extensive-dataset` — `IMDb movies.csv` and `IMDb ratings.csv`.
- MovieLens/TMDB classroom source: `rounakbanik/the-movies-dataset` — `movies_metadata.csv`, `links_small.csv`, `ratings_small.csv`.

When IMDb Kaggle downloading fails, I use a **pinned public Kaggle-data mirror**, verifying the two documented SHA-256 fingerprints in [my provenance report](IMDb_DATA_PROVENANCE.json). When public MovieLens Kaggle downloading fails, I try a documented public mirror of the three necessary CSVs. I record the resolved origin and verify input columns and counts.

**I prefer the original instructor ZIP whenever it is already provided.** I do not claim that the public MovieLens CSVs are byte-identical to the teacher's ZIP. I do not auto-download the very large `ratings.csv`, because my collaborative model trains and evaluates `ratings_small.csv`. If the teacher ZIP contains `ratings.csv`, I inspect just the first 20,000 rows.

## What happens when the network is unavailable?

I never fabricate academic results. If the main IMDb CSVs cannot be obtained from Kaggle or the verified pinned mirror, I raise a clear error showing the sources attempted. If only optional classroom MovieLens is unavailable, I skip that section and complete the two official IMDb tasks. The notebook can use files already available in Colab, Kaggle Code, or Jupyter with no new downloads.

## My verification boundaries

I ran the new notebook in three clean Jupyter sessions using **synthetic testing fixtures only**:

1. All source files supplied locally: 12/12 code cells, no errors.
2. Both sources returned from a mocked `kagglehub.dataset_download`: 12/12 code cells, no errors.
3. IMDb returned, optional MovieLens unavailable: 12/12 code cells, no errors.

I have **not verified a live download through the public Kaggle service in this offline validation environment**, and I do not claim the notebook contains freshly executed authentic data outputs. To complete my academic submission, I will run all cells in Colab with internet enabled, verify data provenance and output tables, and save the executed `.ipynb`.

Official reference: [Kagglehub download documentation](https://github.com/Kaggle/kagglehub#download-dataset).
