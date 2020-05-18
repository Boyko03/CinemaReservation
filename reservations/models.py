from sqlalchemy import Column, Integer, String
from db import Base


class Reservations(Base):
    __tablename__ = "Reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    projection_id = Column(Integer)
    row = Column(Integer)
    col = Column(Integer)

    free_spaces = None
