# My methodology — Assignment 8

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

I developed and documented one Jupyter notebook with two primary **IMDb Extensive** tasks and a separate **MovieLens/TMDB classroom extension**. I never merge their rating scales or falsely identify cohort-average scores as individual ratings.

## My first task — Content-Based recommendations (IMDb)

I load authentic `IMDb movies.csv` and `IMDb ratings.csv`, validate fields and record hashes. I retain up to 3,000 movies with at least 1,000 votes. I combine genres, directors, actors and descriptions, transform the text using unigram/bigram TF-IDF, and rank cosine similarity against a selected title.

## My second task — Collaborative cohort approximation (IMDb)

IMDb Extensive provides aggregated age/gender audience ratings rather than `userId` histories. I construct a six-cohort-by-film rating matrix, require at least 30 votes for a cohort rating to be usable, and compare cohorts using Pearson correlation. I withhold roughly 15% of observed cells subject to minimum training support, predict the withheld averages from positively correlated groups and compute held-out MAE/RMSE. I compare MAE against a training-cohort-mean baseline.

**Limitation:** I estimate group-level averages, not viewer-personalized preferences or Surprise/SVD predictions.

## My classroom extension — MovieLens/TMDB

I read the original classroom files: `movies_metadata.csv`, `links_small.csv`, `ratings_small.csv` and a bounded first-20,000-row sample of the larger `ratings.csv`. I link metadata with MovieLens IDs, compare text descriptions with TF-IDF, and implement a separate user-based collaborative neighborhood with training-only centering. I evaluate held-out individual user ratings using MAE/RMSE and a paired user-mean baseline.

This extension relates to the instructor's follow-up request to consider both datasets. The specific source names in that email were not explicit, so I label my extra work as an interpretation, not as an additional written task.

## Historical experimental evidence versus current run

The earlier IMDb-only version of my notebook stored an experiment on 85,855 original movie records and a selected sample of 3,000 eligible films, with 2,700 held-out cohort averages, MAE 0.1836 and RMSE 0.2477. Those are **historical results from a previous version**, not independently reproduced metrics for my newly unified notebook.

My updated unified notebook passed two clean Jupyter executions against **explicitly synthetic test fixtures**. I must rerun it with authentic Kaggle CSVs and the instructor ZIP and save authentic output cells before stating that my final unified submission has been executed on both original datasets.

I recorded the earlier IMDb mirror version and recorded SHA-256 checksums in [IMDb data provenance](IMDb_DATA_PROVENANCE.json), and classroom historical evidence in [classroom data verification](CLASSROOM_DATA_VERIFICATION.md).

## References

- Beth Muturi, classroom Assignment 8 notebook.
- [Stefano Leone, IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Rounak Banik, Movie Recommender Systems](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems).
