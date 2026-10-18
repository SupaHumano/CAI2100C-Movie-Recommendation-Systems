<div align="center">

# Movie Recommendation Systems | Assignment 8

**Juan Luna Santibanez**

Miami Dade College | CAI2100C-2267-6908 | Machine Learning Foundations

**Professor Beth Muturi**

**Goal:** Build and compare content-based and collaborative movie recommendation systems using the IMDb Extensive dataset.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white) ![Methods](https://img.shields.io/badge/Content%20%2B%20Collaborative-Recommendations-18a999)

[**Google Colab**](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb) · [**Jupyter Notebook**](notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb) · [**IMDb Dataset**](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset) · [**Interactive Demo**](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)

</div>

![Movie Recommendation Systems](assets/hero.svg)

[![Interactive movie recommendation lab preview](assets/site-preview.svg)](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)

---

[Overview](#overview) · [Task 1](#task-1-content-based-recommendations) · [Task 2](#task-2-collaborative-recommendations) · [Interactive Demo](#interactive-demo) · [Run](#run-the-notebook) · [Files](#project-files) · [References](#references)

## Overview

In this assignment, I explore two approaches to movie recommendations. One compares what movies are about, while the other uses patterns in ratings. I use the **IMDb Extensive Dataset** referenced in the course assignment and keep the examples from our classroom notebook separate.

The Jupyter notebook contains my Python implementation and figures. I also created an interactive example to make the two approaches easier to understand.

![Two approaches to movie recommendations](assets/methods.svg)

## Task 1: Content-Based Recommendations

I compare movies using their descriptions, genres, directors, and actors. **TF-IDF** converts the text into numerical features, and **cosine similarity** finds titles with related content. The similarity score does not represent someone's personal rating.

![Content-based workflow](assets/content.svg)

## Task 2: Collaborative Recommendations

Collaborative filtering normally uses patterns in audience ratings. The IMDb Extensive dataset provides average ratings for **audience cohorts**, rather than individual viewer histories. I use a cohort-level collaborative approximation to compare those patterns without claiming that it predicts what one person would choose.

![Collaborative filtering](assets/collaborative.svg)

## Interactive Demo

The [movie recommendation lab](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/) lets me switch between content-based and cohort-rating examples. I designed it with a cinematic movie catalog, selectable titles, and visual recommendation cards. **All demo movie titles and scores are fictional.** The actual IMDb data is used in the notebook only when the original Kaggle CSV files are provided.

![Movie Lab recommendation comparison](assets/lab-preview.svg)

## Verified Classroom Dataset Experiment

I also ran both recommendation approaches using the original MovieLens/TMDB files provided for class. These real classroom results are recorded separately in [Classroom Data Verification](docs/CLASSROOM_DATA_VERIFICATION.md), together with a [reproducible classroom notebook](notebooks/Assignment_8_Classroom_Data_Verification.ipynb). Those CSVs are not the IMDb Extensive files required by the final tasks, and the results are not represented as IMDb Extensive results.

## Run the Notebook

### Google Colab

[Open the notebook in Google Colab](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/main/notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb), upload **IMDb movies.csv** and **IMDb ratings.csv** from [Kaggle](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset), and select **Runtime → Run all**.

### Kaggle

Open [Kaggle Code](https://www.kaggle.com/code), import the notebook, and attach the [IMDb Extensive dataset](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset). This project does not claim that a separate Kaggle notebook is already published.

### Local Jupyter

```bash
git clone https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems.git
cd CAI2100C-Movie-Recommendation-Systems
python -m pip install -r requirements.txt
jupyter notebook notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb
```

Place the two original IMDb CSV files in the local `data/` folder first.

## What I Learned

Content-based filtering finds related movies from their information. The other method estimates patterns in audience ratings. The results depend on what the dataset contains, so I explain the difference between aggregated cohort averages and individual preferences.

I keep the methods and explanations together so I can reproduce this assignment and review the concepts later.

## Project Files

```text
CAI2100C-Movie-Recommendation-Systems/
├── README.md
├── index.html
├── notebooks/
│   ├── Assignment_8_Movie_Recommendation_Systems.ipynb
│   └── Assignment_8_Classroom_Data_Verification.ipynb
├── src/
│   └── recommenders.py
├── assets/
│   ├── hero.svg
│   ├── methods.svg
│   ├── content.svg
│   ├── collaborative.svg
│   ├── site-preview.svg
│   ├── lab-preview.svg
│   ├── icon.svg
│   └── posters/ (9 original fictional film posters)
├── data/
│   ├── demo.js
│   └── demo_fictional.json
├── docs/
│   ├── PRESENTATION_GUIDE.md
│   ├── METHODOLOGY.md
│   ├── ASSIGNMENT_REQUIREMENTS.md
│   ├── CLASSROOM_DATA_VERIFICATION.md
│   └── KAGGLE_NOTEBOOK_REFERENCES.md
├── requirements.txt
└── .gitignore
```

## Data Sources and Reproducibility

The [primary notebook](notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb) is designed to run with the original IMDb Extensive Kaggle CSV files. Those files are not redistributed in this repository, and measured results from IMDb Extensive will be available only after that dataset is supplied.

The [classroom experiment](notebooks/Assignment_8_Classroom_Data_Verification.ipynb) uses the MovieLens/TMDB CSV files from the instructor's course materials. Its measured results are explained separately in [Classroom Dataset Results](docs/CLASSROOM_DATA_VERIFICATION.md). These source files are not the same as IMDb Extensive.

My [question-and-answer guide](docs/PRESENTATION_GUIDE.md), [methodology](docs/METHODOLOGY.md), and [Kaggle notebook references](docs/KAGGLE_NOTEBOOK_REFERENCES.md) provide the concepts and sources for this assignment.

## References

- Miami Dade College, *Machine Learning Foundations*, Assignment 8, Professor Beth Muturi.
- [Kaggle: IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [scikit-learn: TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
- [scikit-learn: Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html).

---

**Juan Luna Santibanez | Miami Dade College | CAI2100C**