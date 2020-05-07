CREATE_USERS = """
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY NOT NULL,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(64) NOT NULL
    );
"""
