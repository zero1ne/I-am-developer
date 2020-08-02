from call import Call
from feepolicy import FeePolicy
from typing import List


class RatePolicy():
    def calcuate_fee(self, calls: List[Call]) -> int:
        raise NotImplementedError()


class BasePolicy(RatePolicy):
    def __init__(self, fee_policies: List[FeePolicy]) -> int:
        self.fee_policies = fee_policies

    def calcuate_fee(self, calls: List[Call]) -> int:
        fee = 0
        for fee_policy in self.fee_policies:
            fee += fee_policy.calculate_fee(calls)
        return fee
