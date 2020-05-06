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
        db.cursor.execute(query, (username, password))

        user_id = db.cursor.fetchone()[0]
        db.connection.close()

        if user_id is not None:
            return self.model(user_id, username, password)

    def sign_up(self, username, password):
        query = """
        INSERT INTO Users
        (username, password)
        VALUES(?, ?);
        """

        db = Database()
        db.cursor.execute(query, (username, password))

        db.connection.commit()
        db.connection.close()

        return self.login(username, password)
