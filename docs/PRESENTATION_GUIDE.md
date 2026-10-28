# My presentation — Assignment 8

**Juan Luna Santibanez** · Miami Dade College · CAI2100C · Professor Beth Muturi

## Introduction

I built two movie recommendation approaches using an authentic selected IMDb Extensive research sample. My source dataset is stored in two separate CSV files, as in my Assignment 7 project. My notebook focuses on the actual algorithms, charts, experiments and conclusions.

## Task 1 — Content-Based Filtering

I represent each film by metadata describing its genre, director, actors and story. TF-IDF transforms the text into numeric features. Cosine similarity produces a list of films with similar characteristics. My notebook shows ten recommendations and a bar chart.

## Task 2 — Collaborative Filtering

I examine IMDb's available age/gender **aggregate rating patterns** using Pearson correlation between groups. I evaluate hidden observed averages with MAE, RMSE and a training-mean baseline. IMDb Extensive does not supply individual viewer histories, so my output estimates group averages rather than personal preferences.

## Data and scope

I used 3,000 authentic selected IMDb films and 3,000 matching cohort-rating rows. The research sample favors highly voted movies. I do not claim to have processed every film in IMDb Extensive.

## Running the project

The independent ZIP contains my notebook and both CSV files. I open the notebook in Jupyter, VS Code, or another compatible IDE and choose Run all. In Colab, opening only the GitHub notebook automatically downloads the missing CSVs from the same repository. This is the same method used in Assignment 7.

## Final conclusion

Content-Based Filtering compares *movie attributes*; my rating-pattern approach compares *observed group averages*. Both methods illustrate different ideas behind movie recommendation. I report their inputs and limits without confusing group ratings with individual user preferences.

[My notebook](../notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb) · [My project](https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems)
