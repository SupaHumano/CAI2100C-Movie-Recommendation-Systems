<div align="center">

# Movie Recommendation Systems — Assignment 8

### CAI2100C-2267-6908 · Machine Learning Foundations

**Juan Luna Santibanez**  
**Miami Dade College | Professor Beth Muturi**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-TF--IDF%20%2B%20Collaborative-F7931E?logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-One_Executed_Notebook-F37626?logo=jupyter&logoColor=white)
![MDC](https://img.shields.io/badge/MDC-CAI2100C-173B69)
![Status](https://img.shields.io/badge/Data-Verified_Offline_Research_Snapshots-25805C)

**Two final IMDb tasks. One independent MovieLens extension. One self-contained notebook.**

*How do movie characteristics and audience rating patterns generate different recommendations?*

[**Google Colab**](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb) · [**Download notebook on GitHub**](notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb) · [**Data provenance**](docs/OFFLINE_PROVENANCE.json) · [**Live educational demo**](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)

</div>

![My Assignment 8 academic cover](assets/assignment8-cover.svg)

---

[Overview](#overview) · [Tasks](#my-two-final-assignment-tasks) · [Classroom](#my-separate-classroom-extension) · [Data](#embedded-authentic-research-subsets) · [Validation](#what-i-verified) · [Run](#run-the-exact-notebook-i-submitted) · [Presentation](#my-presentation) · [Sources](#academic-references)

## Overview

I built **one fully executed Jupyter notebook** containing two final IMDb Extensive recommendation tasks and a separately labeled MovieLens/TMDB classroom extension. I identified and verified the **original IMDb source CSVs by SHA-256** before extracting the exact research rows needed for my experiments.

I embedded the resulting genuine **research snapshots** into the notebook itself. I do **not** mislabel the snapshots as the entire 85,855-film original IMDb database or claim to include the complete instructor ZIP. This distinction makes the analysis both reproducible and academically transparent.

**This notebook no longer requires Kaggle login, network access to download data, file uploads, or a teacher ZIP.** Opening it in Colab and choosing **Runtime → Run all** extracts the embedded source snapshots, checks their SHA-256 hashes, runs the mathematical methods and recreates its metrics and charts.

![My project lab preview](assets/assignment8-lab-preview.svg)

## My two final assignment tasks

| Task | My method | Dataset | What I evaluate |
|:--|:--|:--|:--|
| **1 — Content-Based** | TF-IDF on genres, descriptions, actors and directors; cosine similarity | IMDb Extensive research snapshot | Related-title ranking and similarity chart |
| **2 — Collaborative** | Pearson similarity among six age/gender rating cohorts | IMDb Extensive rating snapshot | Held-out cohort-average MAE/RMSE and training-only mean baseline |

**Scientific limitation:** IMDb Extensive provides *group-level average ratings*, not each viewer's identity and film ratings. My cohort-based method is an **approximation**, not individual-personalized collaborative filtering or SVD. I explicitly distinguish these targets.

### Task 1 — My content-based recommendations

![Metadata-to-similarity workflow](assets/content.svg)

I convert film metadata into text features with `TfidfVectorizer`, then rank other films using cosine similarity to the selected film. The similarity score measures characteristics of items, not a person's satisfaction.

### Task 2 — My cohort-rating approximation

![Cohort patterns workflow](assets/collaborative.svg)

I create a six-cohort rating matrix, exclude observations with insufficient cohort votes, calculate Pearson correlations and validate estimates on withheld observed cohort averages. I report a training-only baseline instead of claiming predictive advantage without a comparison.

## My separate classroom extension

My instructor's lesson used MovieLens/TMDB to demonstrate recommenders on **individual viewer ratings**. I included a separately labeled extension because the follow-up email requested “both datasets” without naming them. The two final tasks in the supplied assignment notebook both reference IMDb Extensive.

In my MovieLens/TMDB extension, I compare movie overview text and evaluate **user-neighborhood collaborative filtering** on held-out individual movie ratings. This is **not** the Surprise/SVD implementation from the lecture; I disclose the algorithmic distinction. The public Kaggle-derived snapshots are not claimed byte-identical to my instructor's original ZIP.

## Embedded authentic research subsets

This is one real-data **research snapshot**, not a fabricated demonstration or a download-at-run-time script. The publicly documented source versions are pinned by their original repository commits. I retain every embedded file's hash in [OFFLINE_PROVENANCE.json](docs/OFFLINE_PROVENANCE.json).

| Embedded file | Source | Authentic research rows |
|:--|:--|--:|
| `IMDb movies.csv` | IMDb Extensive | **3,000** |
| `IMDb ratings.csv` | IMDb Extensive | **3,000** |
| `movies_metadata.csv` | MovieLens/TMDB | **9,099** |
| `links_small.csv` | MovieLens/TMDB | **9,125** |
| `ratings_small.csv` | MovieLens/TMDB | **100,004** |

The original IMDb source was first verified with its **complete-file SHA-256 checksums**; I then selected the 3,000 most-voted eligible movies by a reproducible criterion and matched their cohort rating rows by `imdb_title_id`. For MovieLens, I kept all `ratings_small.csv` rating events and link rows and the metadata associated with those links. The very large `ratings.csv` is unnecessary for this model and is not embedded.

**What this means:** my experiment is performed on clearly documented source subsets, not the complete original datasets. I never present a sample size as a full-dataset size, and I never attribute MovieLens results to IMDb.

## What I verified

I generated the final notebook in a GitHub validation runner, downloading the original real source CSVs from pinned GitHub mirrors. The build passed these gates:

1. **Authentic-source gate:** both complete original IMDb files matched their previously documented SHA-256 fingerprints.
2. **Embedding integrity gate:** all five compressed source snapshots were embedded in one `.ipynb`; each is verified before extraction.
3. **Independent execution gate:** the notebook was executed in a clean temporary directory **without the source CSVs present**. All **13/13 Python code cells** ran without exceptions, and the resulting outputs were saved in that same notebook.

**Results are derived from the documented embedded research subsets.** I distinguish their rating scales: IMDb cohort means are on 1–10; MovieLens individual ratings are on 0.5–5. Their raw MAE/RMSE figures do not measure equivalent prediction targets.

Read the exact [build provenance and checksums](docs/OFFLINE_PROVENANCE.json), [methodology](docs/METHODOLOGY.md) and [presentation guide](docs/PRESENTATION_GUIDE.md).

## Interactive educational lab

[**Open my live Movie Lab**](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/).

The interactive website is an **independently labeled fictional teaching demonstration**. Its imaginary films and scores illustrate recommendation concepts and **are not the recorded IMDb/ MovieLens model outputs**. My executed `.ipynb` contains the authentic numerical evidence.

## Run the exact notebook I submitted

### Google Colab — no data-upload steps

[**Open the single academic notebook in Google Colab**](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).

1. Open the link.
2. Choose **Runtime → Run all**.
3. Review the authentic-snapshot integrity checks, recommendation tables, charts, MAE/RMSE evaluation and conclusions.
4. To submit an updated execution, choose **File → Download → Download .ipynb**.

**All five source snapshots are already stored in the notebook.** No external CSV, ZIP, Kaggle token or network retrieval is required for the data. Standard scientific Python packages must be available in the runtime (as they normally are in Colab).

### Kaggle Code

Import the **same notebook** into Kaggle Code and run it. No separate Kaggle dataset attachment is required because the research snapshots are embedded. I do not claim a separate Kaggle publication URL.

### Local Jupyter

```bash
git clone https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems.git
cd CAI2100C-Movie-Recommendation-Systems
python -m pip install -r requirements.txt
jupyter notebook notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb
```

## My presentation

I present the problem, the distinct datasets, the two final IMDb methods, my optional user-based classroom extension, authentic research snapshots, evaluation limitations and conclusions. My [oral presentation guide](docs/PRESENTATION_GUIDE.md) is consistent with my executable notebook and public website.

## Repository structure

```text
CAI2100C-Movie-Recommendation-Systems/
├── README.md
├── index.html
├── notebooks/
│   └── Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb
├── docs/
│   ├── OFFLINE_PROVENANCE.json
│   ├── METHODOLOGY.md
│   ├── PRESENTATION_GUIDE.md
│   ├── ASSIGNMENT_REQUIREMENTS.md
│   └── archive/  (previous classroom reference, not a second submission)
├── assets/       (original academic cover, illustrations, demo assets)
├── data/         (clearly fictional educational website data)
├── src/          (supporting source reference)
└── requirements.txt
```

## Academic references

- Professor Beth Muturi, *Assignment 8: Movie Recommendation Systems*, CAI2100C, Miami Dade College.
- [Stefano Leone, IMDb Extensive dataset](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Pinned original-data mirror used for verification](https://github.com/Abkas/Machine-Learning-Approaches-for-Movie-Rating-Prediction-on-IMDb-Dataset/tree/509c026e32a6fa78cfc987a0aa39f47cc47fd243/Dataset).
- [Rounak Banik, The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).
- [Rounak Banik, Movie Recommender Systems teaching reference](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems).
- [scikit-learn: TF-IDF vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) and [cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).

---

<div align="center">

**Juan Luna Santibanez**  
Miami Dade College · Machine Learning Foundations · Professor Beth Muturi

*Represent. Compare. Evaluate. Explain.*

</div>
