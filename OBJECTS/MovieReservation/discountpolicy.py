from typing import List

class DiscountPolicy():
    ZERO = 0

    def __init__(self, discount_conditions: List['DiscountCondition']) -> None:
        self._discount_conditions = discount_conditions

    def calc_discount_price(self, screen: 'Screen') -> int:
        for condition in self._discount_conditions:
            if condition.is_satisfied(screen):
                return self._get_discount_price(screen)

        return self.ZERO

    def _get_discount_price(self, screen: 'Screen') -> int:
        raise NotImplementedError()


class AbsoluteDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_price: int, discount_conditions: List['DiscountCondition']) -> None:
        super().__init__(discount_conditions)
        self._discount_price = discount_price

    def _get_discount_price(self, screen: 'Screen') -> int:
        return self._discount_price


class RelativeDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_percent: float, discount_conditions: List['DiscountCondition']) -> None:
        super().__init__(discount_conditions)
        self._discount_percent = discount_percent

    def _get_discount_price(self, screen: 'Screen') -> int:
        return screen.get_movie().get_default_price() * self._discount_percent


class NoneDiscountPolicy(DiscountPolicy):
    def __init__(self) -> None:
        pass

    def get_discount_price(self, screen: 'Screen') -> int:
        return self.ZERO
