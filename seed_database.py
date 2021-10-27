""" Seed Database"""

import os, json, crud, model, server
from random import choice, randint
from datetime import datetime


os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#loop over each dictionary
#args to crud.create_movie
#fix datetime part of data
#create_movie takes title, overview, release_date, poster_path)
#add movies to a list as we go

