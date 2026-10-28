<div align="center">

# Movie Recommendation Systems

### CAI2100C-2267-6908 | Machine Learning Foundations | Assignment 8

**Juan Luna Santibanez**  
**Miami Dade College** | **Professor Beth Muturi**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF%20%2B%20Similarity-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-One_Notebook-F37626?logo=jupyter&logoColor=white)
![Course](https://img.shields.io/badge/MDC-CAI2100C-173B69)
![QA](https://img.shields.io/badge/QA-Synthetic_Smoke_Tested-25805C)

**Two recommendation methods. Two distinct sources. One reproducible notebook.**

*What changes when I recommend a film from its characteristics instead of rating patterns?*

[**Google Colab**](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb) · [**Jupyter Notebook**](notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb) · [**IMDb Dataset**](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset) · [**Interactive Demo**](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)

</div>

![Academic cover: Movie Recommendation Systems, two algorithms and two separate data sources](assets/assignment8-cover.svg)

---

[Overview](#overview) · [Assigned Tasks](#assignment-objectives) · [Methods](#how-my-models-work) · [Evidence](#results-and-evidence) · [Live Lab](#interactive-movie-lab) · [Run](#run-the-notebook) · [Structure](#repository-structure) · [Sources](#references)

## Overview

I built a **single Python/Jupyter notebook** for the two final tasks in Professor Muturi's Assignment 8: a **Content-Based Recommender** and a **Collaborative Recommendation approach** using the assigned [IMDb Extensive dataset](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset). I also included a **separately labeled MovieLens/TMDB classroom extension** in response to the follow-up instruction, *“Please use both datasets.”* The email did not identify the datasets by name; I document my interpretation rather than presenting it as an unambiguous new assignment requirement.

**My key distinction:** IMDb Extensive supplies *average ratings for demographic cohorts*, whereas MovieLens supplies *individual user–movie ratings*. I do not merge their scores, compare the raw errors across their different scales, or claim that cohort averages predict a particular viewer's preference.

## Assignment Objectives

| Scope | My implementation | Dataset | Why it matters |
|:---|:---|:---|:---|
| **Task 1** | TF-IDF + cosine similarity | IMDb Extensive | Find films with similar content |
| **Task 2** | Cohort correlation + held-out prediction | IMDb Extensive | Understand patterns in aggregated ratings |
| **Classroom extension** | Content similarity + user-neighborhood ratings | MovieLens/TMDB | Demonstrate individual user interactions separately |

Both final numbered tasks in the instructor's notebook reference **IMDb Extensive**. The extension is visibly optional in my organization and does **not** replace either final task. The instructor's classroom demonstration uses Surprise/SVD; my neighborhood-based extension is a different collaborative method and I do not describe it as an exact SVD reproduction.

## How My Models Work

### Task 1 — Content-Based

I combine **genre, director, cast and description**, vectorize the text with TF-IDF and rank other titles by cosine similarity. Similarity measures overlap in the chosen text features, **not** the probability that somebody will like a film.

![Two recommendation methods: content and collaborative](assets/methods.svg)

### Task 2 — Collaborative approximation

I build a matrix of six age/gender cohorts by movie. After minimum-vote filtering, I compare cohort patterns with Pearson correlation, use observed neighboring groups to estimate held-out cohort means, and report **MAE and RMSE** alongside a mean-rating baseline. This is *group-level estimation*, not personal recommendation or Surprise SVD.

### My classroom extension — individual ratings

I load the authentic instructor MovieLens/TMDB source, keep it separate from IMDb, and compare item descriptions and user-neighborhood rating predictions. I inspect the large `ratings.csv` using a bounded sample rather than loading it all into memory.

## Results and Evidence

The existing repository preserves figures from an **earlier executed IMDb-only notebook**, which studied 3,000 eligible titles and reported **MAE 0.1836 and RMSE 0.2477** on *held-out cohort averages* (1–10 scale, 2,700 observations). These are *historical results*, **not** fresh outputs from this revised unified notebook.

| Earlier IMDb content-based visualization | Earlier IMDb cohort-correlation visualization |
|:---:|:---:|
| ![Previously computed IMDb content recommendations](assets/imdb-content-recommendations.png) | ![Previously computed IMDb cohort correlation](assets/imdb-cohort-correlation.png) |

I retained the exact [IMDb dataset provenance and recorded SHA-256 values](docs/IMDb_DATA_PROVENANCE.json) and the earlier [classroom verification](docs/CLASSROOM_DATA_VERIFICATION.md) as source-specific historical evidence.

**Current quality gate:** I validated the renamed, auto-loading notebook with three independent 12/12-cell synthetic-fixture tests: local input files, automatic-loader mock, and IMDb-only with optional MovieLens unavailable. All three completed without Python errors. The auto-loader's real-world network success was **not verified in this offline testing environment**. **The current notebook has not yet saved a new execution with authentic CSVs.** I must run it once online, save the authentic outputs and verify provenance before academic submission.

## Interactive Movie Lab

[**Explore my interactive lab**](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)

I designed an interactive, responsive teaching website where I can select a film, change between content-based and cohort-rating views, and inspect ranked examples. The **nine movie titles, poster graphics and audience scores are fictional**. The browser demonstration is intentionally different from scientific outputs computed by the Python notebook.

![Interactive lab preview](assets/assignment8-lab-preview.svg)

The lab explains both methods and links back to the single canonical notebook, methodology and my oral presentation guide.

## My automatic dataset loading\n\nI retrieve authentic files only: `IMDb movies.csv` and `IMDb ratings.csv` from [Stefano Leone's IMDb Extensive dataset](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset), and when possible, the three modeling files `movies_metadata.csv`, `links_small.csv` and `ratings_small.csv` from [Rounak Banik's public MovieLens/TMDB dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset). I install/import [`kagglehub`](https://github.com/Kaggle/kagglehub) automatically, and use documented public mirrors if Kaggle access fails. I identify the data source for every CSV and check the archived IMDb mirror SHA-256 fingerprints. My original instructor ZIP remains preferred if available; I do not claim a public copy is identical. Downloading requires working internet access and may require Kaggle authorization.\n\n## Run the Notebook

### Google Colab

1. [**Open my single notebook in Colab**](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).
2. I choose **Runtime → Run all**. My notebook first finds attached original files and otherwise uses the official **Kagglehub** downloader to retrieve the two IMDb CSV files automatically. If Kaggle is blocked, I try a documented pinned IMDb GitHub mirror and check its SHA-256 hashes.
3. For my optional MovieLens classroom extension, I use the teacher ZIP when present. Otherwise, I automatically request the three required public MovieLens CSVs from Kaggle, then a public mirror if necessary. I do **not** auto-download the large full `ratings.csv`; my model uses `ratings_small.csv`. If MovieLens access is blocked, the two IMDb tasks still complete.\n4. I verify the data summaries, recommendation tables, plots, metrics and provenance, then **save the executed notebook**.

### Kaggle Notebooks

Open [Kaggle Code](https://www.kaggle.com/code) and import [my single `.ipynb`](notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb). My notebook detects Kaggle's attached files or downloads the named CSVs using `kagglehub`. The original instructor ZIP is optional for the supplementary classroom section. I do not claim that I have published a separate Kaggle notebook URL.

### Local Jupyter

```bash
git clone https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems.git
cd CAI2100C-Movie-Recommendation-Systems
python -m pip install -r requirements.txt
jupyter notebook notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb
```

Place both IMDb CSVs and the unmodified class ZIP in a directory the notebook searches. I do not redistribute the original external CSV files in this repository.

## Repository Structure

```text
CAI2100C-Movie-Recommendation-Systems/
├── README.md                   ← Academic project landing page
├── index.html                  ← Interactive educational lab
├── notebooks/
│   └── Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb  ← ONE active submission
├── assets/
│   ├── assignment8-cover.svg   ← Academic project cover
│   ├── imdb-content-recommendations.png
│   ├── imdb-cohort-correlation.png
│   └── posters/               ← Fictional demo artwork
├── data/                       ← Fictional web demonstration records
├── docs/
│   ├── PRESENTATION_GUIDE.md
│   ├── METHODOLOGY.md
│   ├── ASSIGNMENT_REQUIREMENTS.md
│   ├── IMDb_DATA_PROVENANCE.json
│   ├── CLASSROOM_DATA_VERIFICATION.md
│   └── archive/                ← Earlier classroom notebook preserved
├── src/recommenders.py         ← Earlier reference implementation
└── requirements.txt
```

## References

- Beth Muturi, *Assignment 8: Movie Recommendation Systems*, Machine Learning Foundations, Miami Dade College.
- [Stefano Leone, IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Rounak Banik, Movie Recommender Systems](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems) — classroom-method reference, not my final IMDb dataset.
- [scikit-learn: TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) and [Cosine similarity](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity).
- [My methodology](docs/METHODOLOGY.md) · [My oral presentation guide](docs/PRESENTATION_GUIDE.md) · [Kaggle notebook references](docs/KAGGLE_NOTEBOOK_REFERENCES.md).

---

<div align="center">

**Juan Luna Santibanez**  
Miami Dade College | Machine Learning Foundations | Professor Beth Muturi

*Represent. Compare. Evaluate. Explain.*

</div>