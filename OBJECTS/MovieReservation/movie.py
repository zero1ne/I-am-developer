from datetime import timedelta

class Movie:
    def __init__(self, title: str, length: timedelta, price: int, discount_policy: 'DiscountPolicy') -> None:
        self._title = title
        self._length = length
        self._price = price
        self._discount_policy = discount_policy

    def get_title(self) -> str:
        return self._title

    def get_length(self) -> timedelta:
        return self._length

    def get_default_price(self) -> int:
        return self._price

    def get_discounted_price(self, screen: 'Screen') -> int:
        return self._price - self._discount_policy.calc_discount_price(screen)
    