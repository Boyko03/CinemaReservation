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
        user_id = session.query(Users.id).filter(Users.username == username, Users.password == hashed_password).first()

        if user_id is not None:
            return self.model(id=user_id[0], username=username, password=password)

    def create(self, username, password):
        engine = create_engine("sqlite:///cinema.db")
        Session = sessionmaker(bind=engine)

        session = Session()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = self.model(username=username, password=hashed_password)
        print(user.__dict__)
        print('Here')

        session.add(user)
        session.commit()

        return self.login(username, password)
