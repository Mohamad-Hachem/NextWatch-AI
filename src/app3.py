from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
import models
from databse import engine
from databse import SessionLocal
from models import Movies
from starlette import status
from movie import Movie, MovieRequest


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# creating ouur database dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", status_code=status.HTTP_200_OK)
def get_all_movies(db: db_dependency):
    """returning all the movies in our Database"""
    return db.query(Movies).all()


@app.get("/movies/{movie_id}", status_code=status.HTTP_200_OK)
def get_movie_by_id(db: db_dependency, movie_id: int = Path(gt=0)):
    """this api endpoint to get a specific movie by id"""
    movie = db.query(Movies).filter(Movies.id == movie_id).first()
    if movie:
        return movie
    raise HTTPException(status_code=404, detail='Movie not found')


@app.post("/movie/create_movie", status_code=status.HTTP_201_CREATED)
def create_movie(db: db_dependency, movie_request: MovieRequest):
    """creating a new movie endpoint"""
    movie = Movies(**movie_request.model_dump())

    db.add(movie)
    db.commit()
