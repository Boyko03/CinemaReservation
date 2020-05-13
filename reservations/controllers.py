import ast


from .reservations_gateway import ReservationGateway
from movies.movies_gateway import MovieGateway


class ReservationController:
    def __init__(self):
        self.reservations_gateway = ReservationGateway()
        self.movie = None

    def choose_tickets(self):
        tickets_count = input('Step 1 (User): Choose number of tickets> ')
        valid = self.validate_tickets(tickets_count)
        while not valid:
            print('Invalid amount of tickets')
            tickets_count = input('Step 1 (User): Choose number of tickets> ')
            valid = self.validate_tickets(tickets_count)
            if valid is None:
                return

        return int(tickets_count)

    def validate_tickets(self, tickets_count):
        if tickets_count.isalnum():
            tickets_count = int(tickets_count)
            if tickets_count >= 1 and tickets_count <= 100:
                return True
            else:
                return False

        if tickets_count.lower() != 'cancel':
            return False

    def get_movies(self):
        movies_gateway = MovieGateway()
        movies = movies_gateway.show_movies()
        self.movies_count = len(movies)

        self.movies = movies
        return self.movies

    def choose_movie(self):
        movie_id = input('Step 2 (Movie): Choose a movie> ')
        valid = self.validate_movie_id(movie_id)
        while not valid:
            print('Invalid movie id')
            movie_id = input('Step 2 (Movie): Choose a movie> ')
            valid = self.validate_movie_id(movie_id)
            if valid is None:
                return

        movie_id = int(movie_id)

        for movie in self.movies:
            if movie.id == movie_id:
                self.movie = movie
                break

        return movie_id, self.movie.name

    def validate_movie_id(self, movie_id):
        if movie_id.isalnum():
            movie_id = int(movie_id)
            if movie_id >= 1 and movie_id <= self.movies_count:
                return True
            else:
                return False

        if movie_id.lower() != 'cancel':
            return False

    def get_movie_projections(self, movie_id):
        self.projections = self.reservations_gateway.get_projections(movie_id)
        self.projections_count = len(self.projections)

        return self.projections

    def choose_projection(self):
        projection_id = input('Step 3 (Projection): Choose a projection> ')
        valid = self.validate_projection_id(projection_id)
        while not valid:
            print('Invalid projection id')
            projection_id = input('Step 3 (Projection): Choose a projection> ')
            valid = self.controller.validate_projection_id(projection_id)
            if valid is None:
                return

        return int(projection_id)

    def validate_projection_id(self, projection_id):
        if projection_id.isalnum():
            projection_id = int(projection_id)
            if projection_id >= 1 and projection_id <= self.projections_count:
                return True
            else:
                return False

        if projection_id.lower() != 'cancel':
            return False

    def get_matrix(self, projection_id):
        for projection in self.projections:
            if projection.id == projection_id:
                self.hall = projection.hall
                self.hall = ast.literal_eval(self.hall)
                self.projection = projection
                return self.hall

    def choose_seats(self, tickets_count):
        chosen_seats = 0
        seats = []
        while chosen_seats < tickets_count:
            new_seats = input(
                f'Step 4 (Seats): Choose seat {chosen_seats + 1}> ')
            seats.append(new_seats)
            valid = self.valid_hall(seats[chosen_seats])
            while not valid:
                seats[chosen_seats] = input(
                    f'Step 4 (Seats): Choose seat {chosen_seats + 1}> ')
                valid = self.valid_hall(seats[chosen_seats])
                if valid is None:
                    return

            seats[chosen_seats] = valid
            self.reservations_gateway.take_seat(
                self.projection,
                seats[chosen_seats][0],
                seats[chosen_seats][1], self.hall)

            chosen_seats += 1

        self.seats = seats
        return True

    def valid_hall(self, inp):
        inp = inp.strip()
        if inp != '' and inp[0] == '(' and inp[-1] == ')' and len(inp) > 4:
            inp = inp[1:-1].split(',')
            if len(inp) != 2:
                print('Invalid format. Valid is \'(row, col)\'')
                return False
            else:
                row = inp[0].strip()
                col = inp[1].strip()

                if row.isalnum() and col.isalnum():
                    row = int(row) - 1
                    col = int(col) - 1

                    if (row < 0 or row > 9) or (col < 0 or col > 9):
                        print('Lol...NO!')
                        return False
                    elif self.hall[row][col] != '.':
                        print('This seat is already taken!')
                        return False
                    else:
                        return (row, col)
                else:
                    print('Row and column must be integers.')
                    return False
        else:
            if inp.lower() == 'cancel':
                return

            print('Invalid format. Valid is \'(row, col)\'')
            return False

    def finalize(self):
        print('This is your reservation:')
        # self.movie = (self.movie.name, self.movie.rating)
        print(f'Movie: {self.movie.name} {self.movie.rating}')
        print(
            f'Date and time: {self.projection.date} {self.projection.time} {self.projection.type}')
        print(
            f'Seats: {"".join([str((seat[0] + 1, seat[1] + 1)) for seat in self.seats])}')

        finalize = input('Step 5 (Confirm - type \'finalize\') > ')
        while finalize != 'finalize' and finalize != 'cancel':
            print('Type \'finalize\' to finalize or \'cancel\' to cancel.')
            finalize = input('Step 5 (Confirm - type \'finalize\') > ')

        if finalize == 'finalize':
            self.reservations_gateway.commit()
            return True
        else:
            return False
