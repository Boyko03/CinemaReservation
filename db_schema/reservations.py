CREATE_RESERVATIONS = """
    CREATE TABLE IF NOT EXISTS Reservations(
        id INTEGER PRIMARY KEY NOT NULL,
        user_id INTEGER NOT NULL,
        projection_id INTEGER NOT NULL,
        row INTEGER NOT NULL,
        col INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES User(id),
        FOREIGN KEY(projection_id) REFERENCES Projection(id)
    );
"""
