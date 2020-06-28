from datetime import datetime
from movie import Movie
from reservation import Reservation

class Screen:
    def __init__(self, movie: Movie, sequence: int, start_time: datetime) -> None:
        self._movie = movie
        self._sequence = sequence
        self._start_time = start_time

    def get_movie(self) -> 'Movie':
        return self._movie

    def get_sequence(self) -> int:
        return self._sequence

    def get_start_time(self) -> datetime:
        return self._start_time

    def reservate(self, number: int) -> Reservation:
        return Reservation(
            title=self._movie.get_title(),
            number=number,
            start_time=self._start_time,
            end_time=self._start_time + self._movie.get_length(),
            fixed_price=self._movie.get_default_price() * number,
            paid_price=self._movie.get_discounted_price(self) * number
        )