from bag import Bag
from invitation import Invitation
from ticket import Ticket
from typing import Union

class Audience:
    def __init__(self, bag: Bag) -> None:
        self._bag = bag

    def give_ticket_exchange_item(self, price: int) -> Union[int, Invitation]:
        return self._bag.get_ticket_exchange_item(price)

    def receive_ticket(self, ticket: Ticket) -> None:
        self._bag.save_ticket(ticket)