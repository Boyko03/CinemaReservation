from .models import ReservationModel
from db import Database


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    def take_seat(self, projection, row, col):
        query = """
        UPDATE Projections
        SET hall = ?
        WHERE id = ?;
        """

        projection.hall[row][col] = 'X'

        self.db.cursor.execute(query, (projection.hall, projection.id))

    def commit(self):
        self.db.connection.commit()
