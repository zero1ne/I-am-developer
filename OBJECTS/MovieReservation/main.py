from datetime import datetime, time, timedelta
from movie import Movie
from screen import Screen
from reservation import Reservation
from discountpolicy import AbsoluteDiscountPolicy, RelativeDiscountPolicy
from discountcondition import SequenceDiscountCondition, PeriodDiscountCondition

if __name__ == "__main__":
	policy_absolute = AbsoluteDiscountPolicy(800)
	condition_sequence1 = SequenceDiscountCondition(sequence=1)
	condition_sequence2 = SequenceDiscountCondition(sequence=10)
	condition_period1 = PeriodDiscountCondition(weekday=0, period_start=time(hour=10), peroid_end=time(hour=12))
	condition_period2 = PeriodDiscountCondition(weekday=3, period_start=time(hour=18), peroid_end=time(hour=21))

	avatar = Movie(title="avatar", length=timedelta(hours=2), price=10000, 
		discount_conditions=[condition_sequence1, condition_sequence2, condition_period1, condition_period2], discount_policy=policy_absolute)
	screen_a = Screen(movie=avatar, sequence=2, start_time=datetime(year=2020, month=5, day=5, hour=11))

	reservation1 = screen_a.reservate(2)
