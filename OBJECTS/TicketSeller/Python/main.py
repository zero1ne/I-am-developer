from audience import Audience
from bag import Bag
from invitation import Invitation
from ticket import Ticket
from ticketseller import TicketSeller
from ticketbox import TicketBox

if __name__ == "__main__":
    TICKET_PRICE = 5000

    invitation = Invitation()

    bag_with_invitation = Bag(invitation=invitation)
    bag_with_money = Bag(money=TICKET_PRICE)
    
    hit_audience = Audience(bag=bag_with_invitation)
    non_hit_audience = Audience(bag=bag_with_money)

    ticket1 = Ticket(price=TICKET_PRICE)
    ticket2 = Ticket(price=TICKET_PRICE)

    ticketbox = TicketBox(tickets=[ticket1, ticket2], money=0)
    ticketsellor = TicketSeller(ticketbox=ticketbox)

    ticketsellor.sell_ticket_to_audience(audience=hit_audience)
    ticketsellor.sell_ticket_to_audience(audience=non_hit_audience)

    
