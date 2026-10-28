# My methodology — Assignment 8

**Juan Luna Santibanez** · CAI2100C · Professor Beth Muturi

## My data

I use `data/IMDb movies.csv` and `data/IMDb ratings.csv`. They contain the **full original IMDb Extensive movie and ratings tables, with 85,855 records each**. I do not apply a fixed title sample or popularity-based selection. The cohort model uses observations meeting the stated 30-vote minimum, without shrinking the input catalogue.

My notebook follows Assignment 7's simple loading pattern: it finds local CSV files first and retrieves them from the same GitHub repository only if missing. The dataset records are **not embedded in the Python source code**.

## Task 1 — Content-Based Filtering

I build text features from movie genre, director, cast and descriptions. With `TfidfVectorizer` I create sparse vectors and use cosine similarity to rank movies related to the query. The query itself is excluded, and I display the ten highest-ranked results with a graph. Content similarity is not a prediction of an individual user's personal preference.

## Task 2 — Collaborative Filtering approximation

I construct a group-by-movie matrix from six gender-and-age cohort rating averages. A group/movie observation is included only when it has at least **30 votes**. I calculate Pearson correlation between cohorts with sufficient common rated movies. I withhold approximately **15%** of usable averages, estimate them using training observations and compare MAE/RMSE against a training-group-mean baseline. My conclusions concern *group-average* ratings on IMDb's 1–10 scale.

The IMDb source does not provide `userId–movieId–rating` events; therefore I do **not** claim this is personalized user-neighborhood filtering or SVD.

## My reproducibility check

I executed this notebook **twice from a clean temporary project directory** with its two CSV files present: seven executable cells completed in each test without exceptions, with recommendations, graphs and metrics. When opened by itself in Colab, the notebook obtains these CSVs from my public GitHub repository.

## References

- Professor Beth Muturi, CAI2100C Assignment 8.
- [IMDb Extensive, Stefano Leone](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).
