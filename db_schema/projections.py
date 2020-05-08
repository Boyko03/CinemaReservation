from settings import empty_hall


CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS Projections(
    id INTEGER PRIMARY KEY NOT NULL,
    movie_id INTEGER NOT NULL,
    type VARCHAR(10) NOT NULL,
    date VARCHAR(10) NOT NULL,
    time VARCHAR(10) NOT NULL,
    hall BLOB NOT NULL
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
    );
'''

INSERT_INTO_PROJECTIONS = '''
    INSERT INTO Projections(movie_id, type, date, time, hall) VALUES
                                (1, "3D", "2020-04-01", "19:10", {hall}),
                                (1, "2D", "2020-04-01", "19:00", {hall}),
                                (1, "4DX", "2020-04-02", "21:00", {hall}),
                                (3, "2D", "2020-04-05", "20:20", {hall}),
                                (2, "3D", "2020-04-02", "22:00", {hall}),
                                (2, "2D", "2020-04-02", "19:30", {hall});
'''.format(hall=empty_hall)
