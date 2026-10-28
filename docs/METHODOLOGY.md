# My methodology — Assignment 8

**Juan Luna Santibanez · CAI2100C · Professor Beth Muturi**

## My study scope

I completed the **two IMDb Extensive tasks** explicitly printed at the end of the instructor's assignment notebook. I used a **selected research sample of 3,000 real IMDb movies** and corresponding aggregated cohort rating records. I did **not** claim to model the full source catalog. Sampling high-vote movies changes which titles can be recommended and limits generalizability.

## Simple, self-contained data access

I embedded the two selected CSV files **as plain CSV text inside a folded Jupyter code cell**. I read them with `pandas.read_csv(StringIO(...))`. That is the only data loading step. I do not use external CSV paths, network access, compressed encoded payloads, downloaders or checksum routines in the notebook.

## Task 1 — TF-IDF content recommendations

I combine genre, actors, directors and descriptions; generate sparse TF-IDF unigram/bigram vectors with a bounded vocabulary; and compute cosine similarity for a query movie. I exclude the query itself and display ten related titles with a horizontal similarity bar chart.

## Task 2 — IMDb cohort rating-pattern approximation

My 6×N matrix contains ratings from six age/gender cohort averages where cohort vote count is at least 30. I estimate Pearson correlations using co-observed films and require at least 15 common observations for similarity. I hold out about 15% of the usable cohort averages, calculate similarity using **training cells**, and estimate held-out group means from positively correlated groups. I evaluate MAE, RMSE and a training-group-mean baseline on the 1–10 rating scale. I visualize cohort correlations and display the estimated top movie-group averages.

**Critical limit:** I do not call the approach personalized Collaborative Filtering or SVD. IMDb Extensive lacks the individual user–movie ratings needed for conventional user-based SVD training.

## Verification

I executed the same two-task notebook twice with fresh Jupyter kernels and no attached data files. Both runs completed all seven code cells without exceptions, regenerating tables and figures. The delivered file has its outputs saved.

## Sources

- Beth Muturi, Assignment 8 classroom notebook, Miami Dade College.
- [IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [scikit-learn vectorization](https://scikit-learn.org/stable/modules/feature_extraction.html).
