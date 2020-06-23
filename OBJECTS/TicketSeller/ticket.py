class Ticket:
    def __init__(self, price: int) -> None:
        self._price = price

    def get_price(self) -> int:
        return self._price
