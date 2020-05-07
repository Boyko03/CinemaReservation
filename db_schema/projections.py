CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS Projections(
    id INTEGER PRIMARY KEY NOT NULL,
    movie_id INTEGER NOT NULL,
    type VARCHAR(10) NOT NULL,
    date VARCHAR(10) NOT NULL,
    time VARCHAR(10) NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
    );
'''

INSERT_INTO_PROJECTIONS = '''
    INSERT INTO Projections(movie_id, type, date, time) VALUES
                                (1, "3D", "2020-04-01", "19:10"),
                                (1, "2D", "2020-04-01", "19:00"),
                                (1, "4DX", "2020-04-02", "21:00"),
                                (3, "2D", "2020-04-05", "20:20"),
                                (2, "3D", "2020-04-02", "22:00"),
                                (2, "2D", "2020-04-02", "19:30");
'''
