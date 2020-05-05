INSERT_INTO_MOVIES = '''
    INSERT INTO Movies (name, rating)
                        VALUES
                        ("The Hunger Games: Catching Fire", 7.9),
                        ("Wreck-It Ralph", 7.8),
                        ("Her", 8.3);

'''

INSERT_INTO_MOVIES2 = '''
    INSERT INTO Movies(name, rating) VALUES (?,?);
'''


INSERT_INTO_PROJECTIONS = '''
    INSERT INTO Projectons(movie_id, type, date, time) VALUES
                                (1, "3D", "2020-04-01", "19:10"),
                                (1, "2D", "2020-04-01", "19:00"),
                                (1, "4DX", "2020-04-02", "21:00"),
                                (3, "2D", "2020-04-05", "20:20"),
                                (2, "3D", "2020-04-02", "22:00"),
                                (2, "2D", "2020-04-02", "19:30");
'''

INSERT_INTO_PROJECTIONS2 = '''
    INSERT INTO Projections(move_id, type, date, time) VALUES (?,?,?,?);
'''


INSERT_INTO_USERS = '''
    INSERT INTO Users(name, password) VALUES
			("Martin Angelov", "****"),
                        ("Ivo Donchev", "****"),
                        ("Radoslav Georgiev", "****"),
                        ("Rositza Zlateva", "****");
'''

INSERT_INTO_USERS2 = ''' 
    INSERT INTO Users(name, password) VALUES (?,?)
'''


INSERT_INTO_RESERVATIONS = '''
    INSERT INTO Reservations(user_id, projection_id, row, col) VALUES
			(3, 1, 2, 1),
                        (3, 1, 3, 5),
                        (3, 1, 7, 8),
                        (2, 3, 1, 1),
                        (2, 3, 1, 2),
                        (5, 5, 2, 3),
                        (6, 5, 2, 4);
'''


INSERT_INTO_RESERVATIONS2 = '''
    INSERT INTO Reservations(user_id, projection_id, row, col) VALUES (?,?,?,?);
'''


PRINT_MOVIES_TABLE = '''
    SELECT * FROM Movies ORDER BY rating;
'''

SHOW_MOVIE_ALL_PROJECTIONS = '''
SELECT * FROM Projecions JOIN Movies ON Projections.movie_id = Movies.id;
'''

SHOW_MOVIE_PROJECTIONS_DATE = '''
SELECT * FROM Projecions JOIN Movies ON Projections.movie_id = Movies.id WHERE Projections.date = ? ORDER BY date;
'''

