from datetime import datetime, time, timedelta
from movie import Movie
from screen import Screen
from reservation import Reservation
from discountpolicy import AbsoluteDiscountPolicy, RelativeDiscountPolicy
from discountcondition import SequenceDiscountCondition, PeriodDiscountCondition

if __name__ == "__main__":
	avatar_policy = AbsoluteDiscountPolicy(discount_price=800, discount_conditions=[
        SequenceDiscountCondition(sequence=1),
        SequenceDiscountCondition(sequence=10),
        PeriodDiscountCondition(weekday=0, period_start=time(hour=10), peroid_end=time(hour=12)),
        PeriodDiscountCondition(weekday=3, period_start=time(hour=18), peroid_end=time(hour=21)),
    ])

	avatar = Movie(title="avatar", length=timedelta(hours=2), price=10000, discount_policy=avatar_policy)
	avatar_screen = Screen(movie=avatar, sequence=2, start_time=datetime(year=2020, month=5, day=5, hour=11))

	reservation1 = avatar_screen.reservate(number=2)
	print(reservation1)
