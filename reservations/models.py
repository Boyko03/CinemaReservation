from sqlalchemy import Column, Integer, String
from db import Base


class Reservations(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    projection_id = Column(Integer)
    row = Column(Integer)
    col = Column(Integer)
    hall = Column(String)

    free_spaces
