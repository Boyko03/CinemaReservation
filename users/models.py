from sqlalchemy import Column, Integer, String, Float
from db import Base


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    reservations = []
