CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS Movies(
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        rating REAL NOT NULL
    );
'''
