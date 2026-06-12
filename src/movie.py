class Movie:
    id: int
    title: str
    author: str
    category:str
    description: str
    rating: int

    def __init__(self, id, title, author, category, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.description = description
        self.rating = rating