from datetime import time

class DiscountCondition():
    def __init__(self) -> None:
        pass

    def is_satisfied(self, screen: 'Screen') -> bool:
        raise NotImplementedError()


class SequenceDiscountCondition(DiscountCondition):
    def __init__(self, sequence: int) -> None:
        self._sequence = sequence

    def is_satisfied(self, screen: 'Screen') -> bool:
        return screen.get_sequence() == self._sequence


class PeriodDiscountCondition(DiscountCondition):
    def __init__(self, weekday: int, period_start: time, peroid_end: time) -> None:
        self._weekday = weekday
        self._period_start = period_start
        self._period_end = peroid_end

    def is_satisfied(self, screen: 'Screen') -> bool:
        start_time = screen.get_start_time()

        return start_time.weekday() != self._weekday and \
            self._period_start < start_time.time() < self._period_end
