#Include EDA file here
import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# merge movies and ratings
merged = pd.merge(ratings, movies, on='movieId')

# separate genres into individual columns
genres = merged['genres'].str.get_dummies('|')
merged = pd.concat([merged, genres], axis=1)

merged.drop(['genres',  '(no genres listed)'], axis=1, inplace=True)

# convert rating to int
merged['rating'] = merged['rating'].astype(int)

# add reward column
merged['reward'] = merged['rating'].apply(lambda x: 1 if x > 3 else 0)

# shift reward column next to rating
reward = merged.pop('reward')
merged.insert(3, 'reward', reward)
