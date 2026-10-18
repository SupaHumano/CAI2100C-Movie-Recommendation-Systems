# Methodology | Assignment 8

## Content-Based Method

I represent descriptions, genres, actors and directors using TF-IDF with single words and two-word phrases. Cosine similarity ranks films relative to a chosen film. The notebook uses a bounded sample of films with sufficient votes for manageable computing time.

## Collaborative Method

The assigned IMDb ratings data contains vote averages for six audience cohorts, not identifiable viewers. I create a cohort-by-film matrix and keep each rating only when the cohort has at least 30 votes. Correlation between cohort rating patterns provides a similarity measure. Neighbor information estimates group averages. This is **not individual-user SVD**.

To check the method, I held out **2,700** observed cohort averages and compared estimates with those averages. The recorded run produced **MAE 0.1836** and **RMSE 0.2477** on the 1–10 scale. This evaluation is about **cohort averages**, not specific people's preferences.

## Data Notes

MovieLens CSV files belong to the class example. My notebook uses IMDb movies.csv and IMDb ratings.csv from the IMDb Extensive dataset. The saved execution used a pinned public Kaggle-data mirror because the direct download was blocked. The source link, row counts and SHA-256 fingerprints are recorded in `IMDb_DATA_PROVENANCE.json`. The standalone educational website uses fictional movies and example scores. It does not display measured IMDb results.
