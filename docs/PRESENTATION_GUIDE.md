# My oral presentation guide — Assignment 8

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

## What problem did I solve?
I designed and tested two movie recommendation approaches for the IMDb Extensive tasks and a separately labeled classroom extension using MovieLens/TMDB.

## What did the final assignment require?
I read two final tasks in my instructor's notebook: **Content-Based Filtering** and **Collaborative Filtering**, both referencing IMDb Extensive. In a follow-up email my instructor wrote “Please use both datasets,” so I also included the MovieLens/TMDB classroom example as a separate extension. I did not treat the two sources as one dataset.

## Which data did I use?
For IMDb I use `IMDb movies.csv` and `IMDb ratings.csv`. For my classroom extension I use `movies_metadata.csv`, `links_small.csv`, and `ratings_small.csv`; I inspect only the first 20,000 rows of the large `ratings.csv`.

## What is content-based filtering?
I compare movie metadata. My TF-IDF vectorizer turns movie text into numerical features, and cosine similarity finds related movie titles. Similar text does not guarantee that a particular viewer will enjoy a film.

## What does collaborative filtering mean?
I estimate ratings from shared rating patterns. My MovieLens extension uses individual user–movie ratings and positive similarities among nearby users. My IMDb task has **only aggregate averages by six audience cohorts**; I estimate group means, not personalized viewer scores.

## Did I use the exact Surprise/SVD model from the classroom example?
No. I used a user-neighborhood method for the MovieLens extension, and a cohort correlation method for IMDb. I explain both algorithms honestly and cite the classroom reference instead of claiming that my code reproduces Surprise/SVD.

## How did I evaluate my methods?
I split MovieLens ratings into training and test sets with a fixed random seed; I report coverage, MAE, RMSE, and a training-user-mean baseline. For IMDb I withhold observed cohort averages, estimate them from the remaining cohort matrix, and compare MAE/RMSE to a training-group-mean baseline. I never directly compare error magnitudes across their different rating scales.

## What have I verified on this revision?
I ran the unified notebook twice in a clean Jupyter kernel with **synthetic test fixtures**, without Python exceptions. That is a software smoke test, not a claim of fresh measurement on genuine course data. Before final Canvas submission I must rerun the unified file with authentic CSVs and save its outputs.

## What is on the website?
I built a visual educational demo that uses fictional movie titles and scores. I do not present those numbers as scientific IMDb results.

## What did I learn?
Content-based systems compare item characteristics, whereas collaborative systems compare rating patterns. I learned why raw individual ratings and cohort-average statistics support different levels of personalization.

## Closing statement
My work is organized as **one assignment notebook**, with two IMDb tasks, a separate MovieLens classroom extension, evaluation, and documented limitations. I can explain the calculations, their input sources and their limits in my own words.
