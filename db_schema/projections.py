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
