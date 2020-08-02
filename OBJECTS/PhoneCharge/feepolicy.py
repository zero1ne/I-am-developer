from call import Call
from feecondition import FeeCondition
from typing import List


class FeePolicy():
    def __init__(self, amount: int, seconds: int, condition: FeeCondition) -> None:
        self.amount = amount
        self.seconds = seconds
        self.condition = condition

    def calculate_call_fee(self, calls: List[Call]) -> int:
        fee = 0
        for call in calls:
            fee += self.condition.get_satisfied_seconds(
                call) // self.seconds * self.amount
        return fee
