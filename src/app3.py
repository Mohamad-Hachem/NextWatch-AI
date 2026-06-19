from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from databse import engine
from databse import SessionLocal
from models import Movies


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

@app.get("/")
def get_all_movies(db: db_dependency):
    """returning all the movies in our Database"""
    return db.query(Movies).all()