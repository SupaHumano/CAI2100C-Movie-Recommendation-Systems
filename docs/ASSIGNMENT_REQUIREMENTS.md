# Assignment 8 — Requirements

**Juan Luna Santibanez**  
Miami Dade College · CAI2100C · Professor Beth Muturi

The two tasks printed in my Assignment 8 notebook are:

| Task | My work |
|---|---|
| **1. Content-Based Recommendation System** | IMDb movie metadata → TF-IDF → cosine similarity → 10 recommendations and a chart |
| **2. Collaborative Recommendation System** | IMDb six demographic-rating cohorts → Pearson similarity → held-out predictions with MAE/RMSE and baseline |

I use two ordinary CSV files from my selected IMDb Extensive research sample, stored in `data/`. My Jupyter notebook reads them locally or downloads them from this repository in Google Colab, following the same workflow as Assignment 7.

**Limitation:** the IMDb Extensive cohort data do not identify individual users. My Collaborative Filtering implementation is therefore a **group-average approximation** rather than personalized user-based Collaborative Filtering or SVD.

**Submission:** [My Assignment 8 notebook](../notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).