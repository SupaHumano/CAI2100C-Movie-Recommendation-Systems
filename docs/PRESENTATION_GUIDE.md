# My oral presentation — Assignment 8

**Juan Luna Santibanez · CAI2100C · Professor Beth Muturi**

## What did I build?

I built **one Jupyter notebook** with the **two IMDb Extensive recommender tasks** at the end of my instructor's notebook: Content-Based Filtering and a ratings-pattern collaborative approximation.

## What data do I use?

I included two **human-readable CSV datasets** in the notebook: **3,000 authentic IMDb movies** and **3,000 matching cohort-rating rows**. They are a selected high-vote research sample, not the full IMDb Extensive catalog. The data cell is folded for readability and uses Pandas `StringIO` to load the records without external files.

## Task 1 — Content-Based Filtering

I use movie genre, director, actors and description as text features. TF-IDF weights informative words; cosine similarity ranks titles with related metadata. Textual similarity is not proof that a viewer likes the films.

## Task 2 — Rating-pattern collaborative approximation

I use average IMDb ratings and vote counts for six demographic cohorts. I calculate Pearson similarity between groups and estimate selected group-average ratings. IMDb's published cohort data do not identify individual viewers, so this approach **is not Surprise SVD or a personalized user-based recommender**.

## How did I evaluate my model?

I withhold approximately 15% of valid cohort ratings, preserving enough training observations, and calculate MAE and RMSE on those withheld cohort averages. I compare against a training-group-mean baseline. I also show a cohort-similarity chart. I do not compare numeric cosine similarity directly with prediction errors.

## How can I reproduce the results?

I open the notebook in Colab or Jupyter and select **Run all**. There is no dataset upload, download, token, ZIP, encoding decoder, or additional file preparation. The notebook contains the research data, code, results, graphs, and conclusions.

## Why does the website display fictional movies?

I built the site as a separate teaching illustration; fictional titles and example scores are not IMDb model outputs. The real research numbers and my code are in my notebook.

## What did I learn?

Recommendation design depends on the available data. Content-Based Filtering compares item characteristics; rating-pattern methods compare observed preferences or aggregated responses. IMDb Extensive's cohort averages do not support individual-level personalization.

**My notebook:** [Assignment 8 — Juan Luna Santibanez](../notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).
