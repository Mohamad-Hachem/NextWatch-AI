from fastapi import FastAPI, Path, Query, HTTPException
from movie import Movie, MovieRequest
from helper import give_next_proper_id
from starlette import status


app = FastAPI()

MOVIES = [
    Movie(1,"title 1", "auth 1", "thriller", "this is a nice book", 5),
    Movie(2,"title 2", "auth 1", "thriller", "this is a nice book", 3),
    Movie(3,"title 3", "auth 2", "action", "this is a nice book", 2),
    Movie(4,"title 4", "auth 2", "action", "this is a nice book", 1),
    Movie(5,"title 5", "auth 2", "thriller", "this is a nice book", 5),
    Movie(6,"title 6", "auth 1", "love", "this is a nice book", 4),
]

@app.get("/movies", status_code=status.HTTP_200_OK)
def get_all_movies():
    """this api endpoint to return all movies"""
    return MOVIES


@app.get("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def get_movie(movie_id: int= Path(gt=0)):
    """this api endpoint to return a specific movie"""
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="item not found")


@app.get("/movies/", status_code=status.HTTP_200_OK)
def get_movies_with_specific_rating(movie_rating: int= Query(gt=-1,lt=6)):
    """this api endpoint to fet movies with specific reading"""
    final_movies_list = []
    for movie in MOVIES:
        if movie.rating == movie_rating:
            final_movies_list.append(movie)
    return final_movies_list


@app.put("/movies/update_movie", status_code=status.HTTP_204_NO_CONTENT)
def update_movie(movie: MovieRequest):
    """updating a book with a specific ID"""
    movie_updated = False
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie.id:
            MOVIES[i] = Movie(**movie.model_dump())
            movie_updated = True
    if not movie_updated:
        raise HTTPException(status_code=404, detail="item not found")


@app.delete("/movies/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id :int= Path(gt=0)):
    """this api is to delete a movie with a specific movie_id"""
    movie_deleted = False
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie_id:
            MOVIES.pop(i)
            movie_deleted = True
            break
    if not movie_deleted:
        raise HTTPException(status_code=404, detail="item not found")


@app.post("/create-movie", status_code=status.HTTP_201_CREATED)
def create_movie(movie_request: MovieRequest):
    """this api endpoint is to create a movie"""
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(give_next_proper_id(MOVIES, new_movie))