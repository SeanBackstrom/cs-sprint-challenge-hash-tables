#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # starting location is key
    # destination is value
    route = {}

    for ticket in tickets:
        route[ticket.source] = ticket.destination

    final_route = []

    final_route.append(route["NONE"])

    for i in range(0, length):
        final_route.append(route[final_route[i]])
    final_route = final_route[:-1]

    return final_route




tickets = [
    Ticket("PIT", "ORD" ),
    Ticket("XNA", "CID" ),
    Ticket("SFO", "BHM" ),
    Ticket("FLG", "XNA" ),
    Ticket("NONE", "LAX" ),
    Ticket("LAX", "SFO" ),
    Ticket("CID", "SLC" ),
    Ticket("ORD", "NONE" ),
    Ticket("SLC", "PIT" ),
    Ticket("BHM", "FLG" )]

print(reconstruct_trip(tickets, 9))