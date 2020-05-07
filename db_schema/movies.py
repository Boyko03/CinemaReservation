CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS Movies(
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        rating REAL NOT NULL
    );
'''
INSERT_INTO_MOVIES = '''
            INSERT INTO Movies (name, rating)
                            VALUES
                            ("The Hunger Games: Catching Fire", 7.9),
                            ("Wreck-It Ralph", 7.8),
                            ("Her", 8.3);
        '''
