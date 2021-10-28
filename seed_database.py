""" Seed Database"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    
    title, overview, poster_path = (
        movie["title"], 
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)
    
        
#loop over each dictionary
#args to crud.create_movie (imported)
#fix datetime part of data
#create_movie takes title, overview, release_date, poster_path)
#add movies to a list as we go

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    db_user = crud.create_user(email, password)

    for _ in range(10):
        random_movie= choice(movies_in_db)
        score = randint(1, 5)
        crud.create_rating(db_user, random_movie, score)

        