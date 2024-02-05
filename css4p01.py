#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:13:46 2024

@author: blacksail
"""
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
df.columns = df.columns.str.replace(' ', '_')
df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)
summary_stats = df.describe()
print(summary_stats)

df.to_csv("cleaned_movie_dataset.csv", index=False)
df = pd.read_csv("cleaned_movie_dataset.csv")
highest_rated_movie = df[df['Rating']== df['Rating'].max()]
print(highest_rated_movie[['Title', 'Rating']])

df = pd.read_csv("cleaned_movie_dataset.csv")
average_revenue = df['Revenue_(Millions)'].mean()
print(f"Average revenue of all movies: ${average_revenue:.2f} million")

df = pd.read_csv("cleaned_movie_dataset.csv")
df['Year'] = pd.to_datetime(df['Year'], format='%Y') 
filtered_df = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')] 
average_revenue_2015_2017 = filtered_df['Revenue_(Millions)'].mean()
print(f"Average revenue of all movies from 2015 to 2017: ${average_revenue_2015_2017:.2f} million")


df = pd.read_csv("cleaned_movie_dataset.csv")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
movies_2016 = df[df['Year'].dt.year ==2016]
num_movies_2016 = movies_2016.shape[0]
print("Number of Movies Released in 2016", num_movies_2016)


df = pd.read_csv("cleaned_movie_dataset.csv")
movies_nolan = df[df['Director'] == 'Christopher Nolan']
number_of_movies_nolan = len(movies_nolan)
print("Number of MoviesDirected by Christopher Nolan", number_of_movies_nolan) 


df = pd.read_csv("cleaned_movie_dataset.csv")
high_rated_movies = df[df['Rating'] >= 8.0]
num_high_rated_movies = high_rated_movies.shape[0]
print("Number of Movies with a Rating of at least 8.0", num_high_rated_movies)


df = pd.read_csv("cleaned_movie_dataset.csv")
movies_nolan = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan = movies_nolan['Rating'].median() 
print("The median rating of movies directed by Christopher Nolan", median_rating_nolan)


df = pd.read_csv("cleaned_movie_dataset.csv")
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df_filtered = df.dropna(subset=['Rating'])
average_rating_by_year = df_filtered.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
print('Year with the highest average rating:', year_highest_average_rating)

df = pd.read_csv("cleaned_movie_dataset.csv")
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]
movies_2006_count = len(movies_2006)
movies_2016_count = len(movies_2016)
percentage_increase_between_2006_and_2016 = ((movies_2016_count - movies_2006_count) / movies_2006_count) * 100
print("percentage increase in the number of movies made between 2006 and 2016:", percentage_increase_between_2006_and_2016)


df = pd.read_csv("cleaned_movie_dataset.csv")
all_actors = df['Actors'].str.split(', ', expand=True)
flat_actors = all_actors.values.flatten()
actor_counts = pd.Series(flat_actors).value_counts()
most_common_actor = actor_counts.idxmax()
print(f"Most common actor in all the movies: {most_common_actor}")

df = pd.read_csv("cleaned_movie_dataset.csv")
all_genres = df['Genre'].str.split(', ', expand=True)
flat_genres = all_genres.values.flatten()
unique_genres = pd.Series(flat_genres).unique()
num_unique_genres = len(unique_genres)
print("Number of unique genres in the dataset:", num_unique_genres)
