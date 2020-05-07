CREATE_USERS = """
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    );
"""
