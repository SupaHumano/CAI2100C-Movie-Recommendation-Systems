# Oral presentation guide

**Juan Luna Santibanez | CAI2100C | Professor Beth Muturi**

## What problem did you solve?

I explored two movie recommendation methods using the IMDb Extensive dataset. The first compares movie content, while the second looks for patterns in audience ratings.

## What is a recommendation system?

A recommendation system helps someone discover items that may be relevant to their interests. In my assignment, those items are movies.

## What are the model's inputs?

For content-based filtering, I use descriptions, genres, directors, and actors. For the second approach, I use average ratings and vote counts for different IMDb audience cohorts.

## What is content-based filtering?

It compares characteristics of movies. After choosing a title, I look for other films that share similar information, such as genres or descriptions.

## What does TF-IDF mean?

TF-IDF stands for Term Frequency–Inverse Document Frequency. It turns words into numerical features and gives more weight to terms that help distinguish one description from others.

## What does cosine similarity measure?

It measures similarity between two numerical representations. A higher score means the movies are more alike according to the features I selected. It does not guarantee that a particular person will enjoy both films.

## What is collaborative filtering?

It uses patterns in ratings to estimate what may be relevant. The idea is that similar rating patterns can contain useful information beyond a movie's description.

## What is the difference between individual ratings and cohort averages?

An individual rating records one person's score for a movie. A cohort average combines many ratings within an audience category. The IMDb Extensive file provides the second kind of information.

## Can this model predict a particular person's rating?

No. With this dataset, I can estimate patterns in audience-cohort averages, but I cannot identify what a specific viewer would prefer. I make that limitation explicit.

## How are the two recommendation methods different?

Content-based filtering compares what movies are about. The collaborative approach compares available rating patterns. They work with different data and can lead to different recommendations.

## Why is MovieLens mentioned in the course notebook?

MovieLens is used in the classroom example because it includes viewer-to-movie ratings. The final Assignment 8 tasks point to IMDb Extensive, so I keep the datasets separate.

## How did you check the results?

I checked the input columns, verified the similarity calculations, and tested held-out cohort-average predictions. I also ran automated tests using clearly labeled example data, separate from the original IMDb files.

## Why does the interactive website show fictional titles?

The website is a visual example of how the two approaches work. I label its titles and scores as fictional. Actual IMDb results come from running the Python notebook with the original dataset.

## Short conclusion

Content-based filtering finds movies with similar information, while collaborative filtering uses rating patterns. This assignment helped me understand why the available data matters and why recommendation results need to be interpreted carefully.
