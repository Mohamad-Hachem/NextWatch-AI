from fastapi import FastAPI


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