from fastapi import FastAPI, Body
from movie import Movie, MovieRequest
from helper import give_next_proper_id

app = FastAPI()

MOVIES = [
    Movie(1,"title 1", "auth 1", "thriller", "this is a nice book", 5),
    Movie(2,"title 2", "auth 1", "thriller", "this is a nice book", 3),
    Movie(3,"title 3", "auth 2", "action", "this is a nice book", 2),
    Movie(4,"title 4", "auth 2", "action", "this is a nice book", 1),
    Movie(5,"title 5", "auth 2", "thriller", "this is a nice book", 5),
    Movie(6,"title 6", "auth 1", "love", "this is a nice book", 4),
]

@app.get("/movies")
def get_all_movies():
    """this api endpoint to return all movies"""
    return MOVIES


@app.post("/create-movie")
def create_movie(movie_request: MovieRequest):
    """this api endpoint is to create a movie"""
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(give_next_proper_id(MOVIES, new_movie))