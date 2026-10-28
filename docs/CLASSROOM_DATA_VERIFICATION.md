# Verified classroom dataset run | Assignment 8

**Juan Luna Santibanez**  
Miami Dade College | CAI2100C-2267-6908 | Machine Learning Foundations  
**Professor Beth Muturi**

## Source and interpretation

I ran a separate, reproducible check with the original CSV files from the instructor's **Assignment 8-machinelearning.zip**. These are the **classroom MovieLens/TMDB files**, not the separately assigned **IMDb Extensive** Kaggle CSVs. I did not replace the primary Assignment 8 notebook or claim these results came from IMDb Extensive.

## Real classroom data

| File | Observations |
|---|---:|
| movies_metadata.csv | 45,466 movies / metadata rows |
| ratings_small.csv | 100,004 recorded ratings |
| links_small.csv | 9,125 movie ID mappings |

The 100,004 ratings cover **671 unique users** and **9,066 unique movie IDs**.

## Content-based test

I applied **TF-IDF** to the authentic `overview` fields of the first 4,000 eligible, unique IMDb-ID movie metadata records, with English stop-word filtering, unigrams, bigrams and a 4,000-feature limit. I used **cosine similarity** to rank movies relative to *Toy Story*.

| Similar title | Cosine similarity |
|---|---:|
| Toy Story 2 | 0.4626 |
| Man on the Moon | 0.2271 |
| Malice | 0.1824 |
| Condorman | 0.1811 |
| Rebel Without a Cause | 0.1776 |

Similarity depends on the selected text features and the bounded sample. The results reflect metadata similarity, not a viewer's predicted rating.

## Collaborative test

I also evaluated a **user-user collaborative filtering model** using the *real individual rating records* in `ratings_small.csv`. The experiment used a reproducible 80%/20% random rating holdout (seed 42), user-mean-centered cosine similarity, up to **25 positively similar neighbors**, and predicted ratings clipped to the dataset's 0.5–5 rating scale.

| Metric | Result |
|---|---:|
| Original recorded ratings | 100,004 |
| Test ratings in full split | 20,001 |
| Test ratings with known user and movie in training | 19,259 |
| Collaborative MAE | **0.6851** |
| Collaborative RMSE | **0.9003** |

A smoothed user/movie mean baseline on the entire 20,001-row test split yielded **MAE 0.6916** and **RMSE 0.9013**. Because the eligible prediction sets differ, the baseline and KNN results should not be presented as a rigorously paired performance comparison.

These results are measured from the original classroom CSVs. They are **not** the result of training on the final IMDb Extensive dataset and must not be represented as such.

## Reproducibility

The companion [classroom experiment notebook](archive/Assignment_8_Classroom_Data_Verification.ipynb) reads the original ZIP provided by the instructor and reports the model results. Download or upload the ZIP into the Colab or Jupyter runtime. The repository does not redistribute the 183 MB instructor ZIP or the original movie datasets.

## Limits

This is supplementary verification using the exact class files. The final tasks of the professor's notebook still point to [IMDb Extensive on Kaggle](https://www.kaggle.com/datasets/stefanoleone992/imdb-extensive-dataset). That separate dataset was **not present in the instructor ZIP**, and I have not represented these MovieLens results as IMDb Extensive results.


**Current repository organization:** I preserve the earlier separate classroom notebook in my documentation archive; my only active submission notebook is [Assignment 8 unified](../notebooks/Assignment_8_Movie_Recommendation_Systems.ipynb). The figures above are historical, not fresh results from the new unified file.
