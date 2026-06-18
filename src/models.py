from databse import Base
from sqlalchemy import Column, Integer, String


class Movies(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    author = Column(String)
    category = Column(String)
    description = Column(String)
    rating = Column(Integer)
