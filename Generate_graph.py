# function to for the distance graph with vertices
def construct_graph():
    cordinates = {}
    # call the construct world function
    cordinates = construct_world()
    # neighbour list
    nearby = coll.defaultdict(list)
    # distance list
    width,height = 26,26
    distance = [[10for x in range(width)] for y in range (height)]
    # initialize graph
    graph = {}
    # looping through the entire array to find out the closest 5 neighbours
    for x in range(0, 26):
        # looping to find distance
        for y in range(0, 26):
            # checking if same vertex
            if cordinates["vertex"][x] != cordinates["vertex"][y]:
                # calculate distance for all neighbours
                distance[x][y] = round((sqrt((abs((cordinates["vertex_x"][y]-cordinates["vertex_x"][x])))^2 +
                (abs((cordinates["vertex_y"][y]-cordinates["vertex_y"][x])))^2)),1)
        # random select the number of nearby nodes
        nearby = rand.randint(1,4)
        # arrange smallest first
        idx = np.argpartition(distance, nearby)
        # constructing the graph
        graph[cordinates["vertex"][x]] = {}
        for neighbour in range(0, nearby):
            if distance[x][idx[x][neighbour]] == 0:
               distance[x][idx[x][neighbour]] = .1
            graph[cordinates["vertex"][x]][cordinates["vertex"][idx[x][neighbour]]] = distance[x][idx[x][neighbour]]
    # return graph
    return graph,cordinates
