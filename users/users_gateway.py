import hashlib


from .models import UserModel
from db import Database


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def login(self, username, password):
        query = """
        SELECT id
        FROM Users
        WHERE
            username = ? AND
            password = ?;
        """

        db = Database()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.cursor.execute(query, (username, hashed_password))

        user_id = db.cursor.fetchone()
        db.connection.close()

        if user_id is not None:
            return self.model(user_id[0], username, password)

    def sign_up(self, username, password):
        query = """
        INSERT INTO Users
        (username, password)
        VALUES(?, ?);
        """

        db = Database()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db.cursor.execute(query, (username, hashed_password))

        db.connection.commit()
        db.connection.close()

        return self.login(username, password)
