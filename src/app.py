from fastapi import FastAPI, Body


# creating our Fastapi application 
app = FastAPI()


MOVIES = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science', 'desciption': 'random text'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science', 'desciption': 'random text'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history', 'desciption': 'random text'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math', 'desciption': 'random text'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math', 'desciption': 'random text'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math', 'desciption': 'random text'}
]

@app.get("/api-endpoint")
async def hello_world():
    """function to return hello world"""
    return {'message': 'Hello World!'}


@app.get("/movies")
async def get_all_movies():
    """function to get all the available movies"""
    return MOVIES


@app.get("/movies/movie/{movie_name}")
async def get_movie(movie_name: str):
    """function to get the info about a specific movie name"""
    for movie in MOVIES:
        if movie['title'] == movie_name:
            return movie
    
    return {'message': f'movie: {movie_name} was not found'}


@app.get("/test/{random_name}")
async def testing(random_name):
    """this is for testing"""
    return {'message': f'testing {random_name}'}


@app.get("/movies/2")
async def read_author_category_by_query(movies_name: str, category: str):
    movies_to_return = []
    for book in MOVIES:
        if book.get('title').casefold() == movies_name.casefold() and \
                book.get('category').casefold() == category.casefold():
            movies_to_return.append(book)

    return movies_to_return


@app.post("/movies/create_movie")
async def create_movie(new_movie=Body()):
    MOVIES.append(new_movie)


@app.put("/movies/update_movie")
async def update_book(updated_book=Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == updated_book.get('title').casefold():
            MOVIES[i] = updated_book


@app.delete("/movies/delete_movie/{movie_name}")
async def delete_book(movie_name: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == movie_name.casefold():
            MOVIES.pop(i)
            break