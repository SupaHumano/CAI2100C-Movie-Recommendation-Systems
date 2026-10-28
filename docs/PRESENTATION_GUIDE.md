# My oral presentation guide — Assignment 8

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

## What problem did I solve?
I built an authentic-source **single-file** movie-recommendation study with the two final IMDb Extensive assignment methods, plus a clearly identified MovieLens/TMDB classroom extension. I embedded validated source-data snapshots into the Jupyter notebook, so it runs without downloading CSVs.

## What exactly did my teacher assign?
I read the instructor's notebook: Task 1 asks for **Content-Based Filtering** using IMDb Extensive, and Task 2 asks for **Collaborative Filtering** using IMDb Extensive. A follow-up email requested “both datasets,” so I retained MovieLens/TMDB as a separate classroom extension. I do not claim the email explicitly named both sources.

## Which authentic source records are in my notebook?
My source snapshots include **3,000** selected IMDb movie records, **3,000** corresponding aggregate IMDb rating records, **9,099** MovieLens/TMDB metadata records, **9,125** link rows, and **100,004** user-rating events. I checked full original IMDb SHA-256 fingerprints *before subsetting*, and verify the embedded snapshot hashes when I run the notebook. These are **research subsets**, not the entire original IMDb and class datasets.

## Why can I click Run all with no CSV files?
I embedded compressed CSV research snapshots directly in my notebook. Its first code cell extracts them into temporary storage and checks their fingerprints; all remaining code reads the verified extracted files. No separate CSV, Kaggle account, ZIP or source network access is required. Standard Python scientific dependencies are still needed.

## What is Content-Based Filtering?
I combine descriptions, genres, directors and actors, calculate TF-IDF term weights and use cosine similarity to find movies related to a selected title. Content similarity is not an individual's enjoyment prediction.

## What does Collaborative Filtering mean here?
I compare age/gender **cohort-average** ratings using Pearson correlation. IMDb Extensive does not provide identifiable individual-user rating histories, so my estimates are group-level approximations. I do not mislabel them as Surprise/SVD or individualized recommendations.

## What did I implement in the MovieLens extension?
I use individual user–movie rating events and user-neighborhood similarities with a training/test holdout. This is **not** the exact Surprise SVD algorithm used in the classroom example. My film metadata and MovieLens IDs come from a separate pinned public MovieLens/TMDB collection, not a claimed identical copy of the teacher ZIP.

## How did I validate the models?
I compute similarity rankings for the two content-based sections. For both rating approaches, I withhold observations, compute MAE/RMSE on the appropriate rating scale, and compare against a training-only baseline. I do not directly compare the numeric MAE of IMDb group averages with the MAE of MovieLens individual ratings.

## Was the final file really executed?
Yes. A GitHub validation runner downloaded the genuine pinned CSV sources, checked the complete original IMDb hashes, embedded five research snapshots and executed **13/13 Python code cells in a clean working directory without the source files**. The executed outputs are saved inside the published `.ipynb`. The scientific evidence uses **documented research snapshots**, not all source records.

## Why does my website have fictional movies?
I designed a separate interactive educational lab to explain both approaches. The nine fictional movies and illustration scores are not the real training records or the measured IMDb outputs. The academic research is in the notebook.

## Closing conclusion
I learned why a recommender's input structure determines what it can estimate. Content-Based Filtering finds similarity from film characteristics, whereas Collaborative Filtering searches rating patterns. IMDb aggregate cohorts and MovieLens individual ratings answer different questions; my report makes that limitation explicit.

**My canonical notebook:** [Assignment 8 — Juan Luna Santibanez](../notebooks/Assignment_8_Juan_Luna_Santibanez_Movie_Recommendation_Systems.ipynb).
