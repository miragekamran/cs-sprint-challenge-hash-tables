#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a dictionary to keep the routes
    routes_dict = dict()

    # Create a var called route and set to
    # and an emptry array times the length
    route = [None] * length

    # Loop through the tickets
    # and set the source to the destination
    for ticket in tickets:
        routes_dict[ticket.source] = ticket.destination

    # and set the first index of the route array to the "NONE" index
    # of the routes dictionary
    route[0] = routes_dict["NONE"]

    # Loop through the length starting at 1
    # and set the index of route array to
    # the last index of the route in the routes dictionary
    for i in range(1, length):
        route[i] = routes_dict[route[i-1]]
    return route
