class DiscountPolicy():
    def __init__(self) -> None:
        pass

    def get_discount_price(self, movie: 'Movie') -> int:
        raise NotImplementedError()


class AbsoluteDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_price: int) -> None:
        self._discount_price = discount_price

    def get_discount_price(self, movie: 'Movie') -> int:
        return self._discount_price


class RelativeDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_percent: int) -> None:
        self._discount_percent = discount_percent

    def get_discount_price(self, movie: 'Movie') -> int:
        return movie.get_default_price() * self._discount_percent // 100
