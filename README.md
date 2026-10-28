# Movie Recommendation Systems | Assignment 8

**Juan Luna Santibanez**  
Miami Dade College | CAI2100C-2267-6908 | Machine Learning Foundations  
**Professor Beth Muturi**

I developed **one Jupyter notebook** for my Assignment 8. I complete the two final IMDb Extensive tasks and include my separately labeled MovieLens/TMDB classroom extension, reflecting the follow-up instruction to consider both datasets. I keep all rating scales, input tables, and conclusions separate.

**[Open my notebook in Google Colab (review branch)](https://colab.research.google.com/github/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/assignment8-one-notebook-20261027/notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb)** · **[Jupyter notebook (review branch)](https://github.com/SupaHumano/CAI2100C-Movie-Recommendation-Systems/blob/assignment8-one-notebook-20261027/notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb)** · **[IMDb Extensive on Kaggle](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset)** · **[Interactive teaching demo](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/)**

## My final assignment tasks

### Task 1 — IMDb Content-Based Filtering

I use `IMDb movies.csv` and `IMDb ratings.csv`, validate their structure, and represent genres, descriptions, directors, and actors with TF-IDF. I rank movie similarity using cosine similarity.

### Task 2 — IMDb Collaborative Filtering approximation

The assigned IMDb Extensive ratings file provides demographic **cohort averages**, not individual viewer histories. I compare six groups using Pearson correlation, estimate held-out group averages, and report MAE, RMSE and a mean-rating baseline. I do not claim this is personalized SVD.

## My optional classroom extension

I separately use my instructor's MovieLens/TMDB ZIP: `movies_metadata.csv`, `links_small.csv`, `ratings_small.csv`, and a **bounded first 20,000-row inspection** of `ratings.csv`. I perform content similarity and evaluate user-neighborhood rating predictions. My instructor's classroom walkthrough uses Surprise/SVD; my user-neighborhood implementation is an educational alternative, not an exact SVD reproduction.

My extension responds to the follow-up phrase “Please use both datasets,” which does not identify the two sources explicitly. The **two final graded tasks** in the supplied classroom notebook both point to IMDb Extensive.

## Reproduction and verification

1. Open the **single notebook** in Colab, Kaggle Code, or Jupyter.
2. Upload the **authentic** `IMDb movies.csv`, `IMDb ratings.csv`, and the instructor's `Assignment 8-machinelearning.zip` (or its four extracted CSVs).
3. Run all cells. Both sources are required for a full notebook run. I do not silently fabricate results when inputs are absent.
4. Save the **executed** notebook, review all plots and output cells, and use the appropriate Canvas submission option.

**Quality evidence:** the unified notebook passed Jupyter schema/syntax validation and two full clean-kernel executions with **clearly labeled synthetic fixtures** (12/12 code cells in each run, deterministic). This does **not** establish a fresh run on the authentic course CSVs. The earlier IMDb-only notebook on `main` stored historic real-data outputs (3,000 selected films; held-out cohort MAE 0.1836, RMSE 0.2477), but the unified notebook on this review branch has no cached academic outputs until rerun.

I retain the original [IMDb dataset provenance](docs/IMDb_DATA_PROVENANCE.json) and [classroom verification report](docs/CLASSROOM_DATA_VERIFICATION.md) as **historical evidence**; they are not independently reproduced measurements of this revised notebook.

## My presentation and interpretation

I use my [oral presentation guide](docs/PRESENTATION_GUIDE.md), [methodology](docs/METHODOLOGY.md), and [requirements mapping](docs/ASSIGNMENT_REQUIREMENTS.md) to explain what I did and what I cannot infer. The [interactive demonstration](https://supahumano.github.io/CAI2100C-Movie-Recommendation-Systems/) contains **fictional titles and scores**, not measured IMDb recommendations.

## References

- Beth Muturi, *Assignment 8 / Movie Recommendation Systems* classroom notebook and lecture materials, CAI2100C.
- [Stefano Leone, IMDb Extensive](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset).
- [Rounak Banik, Movie Recommender Systems](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems).
- [scikit-learn, TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).

**Juan Luna Santibanez | CAI2100C**
