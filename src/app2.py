from fastapi import FastAPI, Path, Query
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


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int= Path(gt=0)):
    """this api endpoint to return a specific movie"""
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    return "No movies found"


@app.get("/movies/")
def get_movies_with_specific_rating(movie_rating: int= Query(gt=-1,lt=6)):
    """this api endpoint to fet movies with specific reading"""
    final_movies_list = []
    for movie in MOVIES:
        if movie.rating == movie_rating:
            final_movies_list.append(movie)
    return final_movies_list


@app.put("/movies/update_movie")
def update_movie(movie: MovieRequest):
    """updating a book with a specific ID"""
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie.id:
            MOVIES[i] = Movie(**movie.model_dump())


@app.delete("/movies/{movie_id}")
def delete_movie(movie_id :int= Path(gt=0)):
    """this api is to delete a movie with a specific movie_id"""
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie_id:
            MOVIES.pop(i)
            break


@app.post("/create-movie")
def create_movie(movie_request: MovieRequest):
    """this api endpoint is to create a movie"""
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(give_next_proper_id(MOVIES, new_movie))