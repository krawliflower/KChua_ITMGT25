def relationship_status(from_member, to_member, social_graph):
    
    one = social_graph.get(from_member).get("following")
    two = social_graph.get(to_member).get("following")

    if from_member in two and to_member in one:
        status = "friends"
    elif from_member in two:
        status = "followed by"
    elif to_member in one:
        status = "follower"
    else:
        status = "no relationship"
    return status

def tic_tac_toe(board):
    row = len(board)
    o = []
    x = []
    
    for i in range (0,row):
        o.append("O")
        x.append("X")  

    #horizontal
    for i in board:
        if i == o:
            return("O")
            break
        elif i == x:
            return("X")
            break

    #vertical
    for i in range(0,row):
        col = []
        m = 0
        while m < row:
            thing = board[m]
            col.append(thing[i])
            m = m + 1
        if col == o:
            return("O")
            break
        elif col == x:
            return("X")
            break

    #diagonal left to right
    lr = []
    rl = []
    for i in range(0,row):
        thing = board[i]
        lr.append(thing[i])

        thing2 = board[row-1-i]
        rl.append(thing[row-1-i])
        
    if lr == o or rl == o:
        return("O")
        
    elif lr == x or rl == x:
        return("X")
    else:
        return("NO WINNER")

def eta(first_stop, second_stop, route_map):

    route = list(route_map.keys())
    stops = len(route)
    
    for i in route:
        if i[0] == first_stop:
            location = i
            break

    for i in route:
        if i[1] == second_stop:
            destination = i
            break

    position = route.index(location)
    
    time = 0
    while location != destination:
        time = time + route_map.get(location).get("travel_time_mins")
        position = (position + 1) % stops
        location = route[position]

    time = time + route_map.get(destination).get("travel_time_mins")
    
    return time