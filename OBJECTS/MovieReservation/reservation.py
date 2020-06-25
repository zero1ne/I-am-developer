from datetime import datetime

class Reservation:
    def __init__(self, title: str, number: int, start_time: datetime, end_time: datetime, fixed_price: int, paid_price: int) -> None:
        self._title = title
        self._number = number
        self._start_time = start_time
        self._end_time = end_time
        self._fixed_price = fixed_price
        self._paid_price = paid_price

    def __str__(self):
        return "{} {} {} {} {} {}".format(
            self._title, self._number, self._start_time, self._end_time, self._fixed_price, self._paid_price
        )