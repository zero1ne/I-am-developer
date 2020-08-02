from call import Call
from typing import List
from ratepolicy import RatePolicy


class Phone():
    def __init__(self, calls: List[Call], rate_policy: RatePolicy):
        self.calls = calls
        self.rate_policy = rate_policy

    def calcuate_fee(self) -> int:
        return self.rate_policy.calcuate_fee(self.calls)
