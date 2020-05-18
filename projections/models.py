from sqlalchemy import Column, Integer, String
from db import Base


class Projections(Base):
    __tablename__ = 'Projections'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    projection_type = Column(String)
    projection_date = Column(String)
    projection_time = Column(String)
    hall = Column(String)
