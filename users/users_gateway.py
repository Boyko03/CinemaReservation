from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib


from .models import Users


class UserGateway:
    def __init__(self):
        self.model = Users

    def login(self, username, password):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_id = session.query(Users.id).filter(Users.username == username, Users.password == hashed_password).one()

        if user_id is not None:
            return self.model(user_id[0], username, password)

    def sign_up(self, username, password):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = self.model(username=username, password=hashed_password)

        session.add(user)
        session.commit()

        return self.login(username, password)
