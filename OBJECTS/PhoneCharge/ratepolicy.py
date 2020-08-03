from call import Call
from feepolicy import FeePolicy
from typing import List


class BasePolicy():
    def __init__(self, fee_policies: List[FeePolicy]) -> int:
        self.fee_policies = fee_policies

    def calcuate_fee(self, calls: List[Call]) -> int:
        fee = 0
        for fee_policy in self.fee_policies:
            fee += fee_policy.calculate_fee(calls)
        return fee


class AddtionalPolicy():
    def apply_policy_to_fee(self, fee: int) -> int:
        NotImplementedError()


class TaxPolicy(AddtionalPolicy):
    def __init__(self, tax_ratio: float) -> None:
        self.tax_ratio = tax_ratio

    def apply_policy_to_fee(self, fee: int) -> int:
        return fee * (1 + self.tax_ratio)


class DiscountPolicy(AddtionalPolicy):
    def __init__(self, discount_amount: int) -> None:
        self.discount_amount = discount_amount

    def apply_policy_to_fee(self, fee: int) -> int:
        return fee - self.discount_amount
