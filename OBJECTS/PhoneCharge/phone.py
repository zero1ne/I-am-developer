from call import Call
from typing import List
from ratepolicy import AdditionalPolicy, BasePolicy


class Phone():
    def __init__(self, calls: List[Call], base_policy: BasePolicy, additional_policies: List[AdditionalPolicy]) -> None:
        self.calls = calls
        self.base_policy = base_policy
        self.addtional_policies = additional_policies

    def calcuate_fee(self) -> int:
        fee = self.base_policy.calcuate_fee(self.calls)
        for policy in self.addtional_policies:
            fee = policy.apply_policy_to_fee(fee)
        return fee
