from movie import Movie
from typing import List

def give_next_proper_id(movies: List, movie: Movie)-> Movie:
    """This function is to return the right id for next movie"""
    if len(movies) < 1:
        movie.id = 1
        return movie
    else:
        movie.id = movies[-1].id + 1
        return movie