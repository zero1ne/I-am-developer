from invitation import Invitation
from ticket import Ticket
from error import NotEnoughMoneyError
from typing import Optional, Union

class Bag:
    def __init__(self, invitation: Optional[Invitation] = None, money: int = 0, ticket: Optional[Ticket] = None) -> None:
        self._invitation = invitation
        self._money = money
        self._ticket = ticket

    def get_ticket_exchange_item(self, price: int) -> Union[int, Invitation]:
        if self._invitation:
            invitation = self._invitation
            return invitation
        else:
            if self._money >= price:
                self._money -= price
                return price
            else:
                raise NotEnoughMoneyError()

    def save_ticket(self, ticket: Ticket) -> None:
        self._ticket = ticket
