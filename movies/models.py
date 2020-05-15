from sqlalchemy import Column, Integer, String, Float
from db import Base


class Movies(Base):
    __tablename__ = "Movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "[ {} ] - {} - {}".format(Movies.id, Movies.name, Movies.rating)
