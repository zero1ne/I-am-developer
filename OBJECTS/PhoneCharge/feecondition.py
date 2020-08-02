from call import Call
from datetime import datetime, time, timedelta
from typing import List, Optional


class FeeCondition():
    def get_satisfied_seconds(self, call: Call) -> int:
        raise NotImplementedError()


class FeeConditionByFix(FeeCondition):
    def __init__(self) -> None:
        pass

    def get_satisfied_seconds(self, call: Call) -> int:
        return (
            call.get_end() - call.get_start()
        ).second


class FeeConditionByTime(FeeCondition):
    def __init__(self, start: time, end: time) -> None:
        self.start = start
        self.end = end

    def get_satisfied_seconds(self, call: Call) -> int:
        second = 0

        call_start = call.get_start()
        call_end = call.get_end()

        call_start_date = call_start.date()
        call_end_date = call_end.date()

        while call_start_date < call_end_date:
            second += (
                min(datetime.combine(call_start_date, self.end), call_end) -
                max(datetime.combine(call_start_date, self.start), call_start)
            ).second
            call_start_date += timedelta(days=1)

        return second


class FeeConditionByDayOfWeek(FeeCondition):
    def __init__(self, dayofweek: List[int]) -> None:
        self.dayofweek = dayofweek

    def get_satisfied_seconds(self, call: Call) -> int:
        second = 0

        call_start = call.get_start()
        call_end = call.get_end()

        call_start_date = call_start.date()
        call_end_date = call_end.date()

        while call_start_date < call_end_date:
            if call_start_date.weekday() in self.dayofweek:
                second += (
                    min(datetime.combine(call_start_date, time(
                        hour=0, minute=0, second=0)), call_end) -
                    max(datetime.combine(call_start_date, time(
                        hour=23, minute=59, second=59)), call_start)
                ).second
            call_start_date += timedelta(days=1)

        return second


class FeeConditionByInterval(FeeCondition):
    def __init__(self, start: int, end: int) -> int:
        self.start = start
        self.end = end

    def get_satisfied_seconds(self, call: Call) -> int:
        second = (
            call.get_end() - call.get_start()
        ).second

        if second <= self.start:
            return self.start
        elif second <= self.end:
            return second - self.start
        else:
            return second - self.end
