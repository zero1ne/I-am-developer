from audience import Audience
from ticketbox import TicketBox

class TicketSeller:
    def __init__(self, ticketbox : TicketBox) -> None:
        self._ticketbox = ticketbox

    def sell_ticket_to_audience(self, audience : Audience) -> None:
        ticket = self._ticketbox.get_ticket()
        price = ticket.get_price()
        item = audience.give_ticket_exchange_item(price)

        if isinstance(item, int):
            self._ticketbox.add_money(item)

        audience.receive_ticket(ticket)
