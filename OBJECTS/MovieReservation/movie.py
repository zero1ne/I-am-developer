from datetime import timedelta
from typing import List, Optional

class Movie:
    def __init__(self, title: str, length: timedelta, price: int, discount_conditions: Optional[List['DiscountCondition']], discount_policy: Optional['DiscountPolicy']) -> None:
        self._title = title
        self._length = length
        self._price = price
        self._discount_conditions = discount_conditions
        self._discount_policy = discount_policy

    def get_title(self) -> str:
        return self._title

    def get_length(self) -> timedelta:
        return self._length

    def get_default_price(self) -> int:
        return self._price

    def get_discounted_price(self, screen: 'Screen') -> int:
        discount_price = 0
        if self._discount_policy:
            for discount_condition in self._discount_conditions:
                if discount_condition.is_satisfied(screen):
                    discount_price = self._discount_policy.get_discount_price(self)
                    break
        
        return self._price - discount_price
    