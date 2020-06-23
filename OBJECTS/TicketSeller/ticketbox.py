from ticket import Ticket
from error import NoMoreTicketError
from typing import List

class TicketBox:
    def __init__(self, tickets : List[Ticket], money: int) -> None:
        self._tickets = tickets
        self._money = money

    def get_ticket(self) -> Ticket:
        if self._tickets:
            return self._tickets.pop()
        else:
            raise NoMoreTicketError()
    
    def add_money(self, money) -> None:
        self._money += money
