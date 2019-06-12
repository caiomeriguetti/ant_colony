
from test_data import PathData
import random

evaporation_rate = 0.5

nodes = 10

graph1 = PathData(nodes)

ants = 1

iterations = 1
for i in range(0, iterations):
    paths = []
    for j in range(0, ants):

        # visiting nodes
        start_node = random.randint(0, nodes - 1)
        already_visited = set()
        queue = []
        queue.append(start_node)
        path = []
        while len(queue) > 0:
            node = queue.pop(0)

            path.append(node)

            #selecting a random connected node to visit
            connection_costs = graph1.costs[node]
            possible_connections = range(0, len(connection_costs))
            while len(possible_connections) > 0:
                random_possible_connection = possible_connections.pop(
                    random.randint(0, len(possible_connections)-1)
                )

                if connection_costs[random_possible_connection] is not None \
                   and random_possible_connection not in already_visited:
                    queue.append(random_possible_connection)

            already_visited.add(node)

        paths.append(path)

    #feromon evaporation
    for line in graph1.feromon:
        for i in range(0, len(line)):
            line[i] *= (1.0 - evaporation_rate)

    #feromon deposit
    for path in paths:
        # path length
        current_node = path[0]
        total_path_cost = 0
        for i in range(1, len(path)):
            total_path_cost += graph1.costs[current_node][path[i]]
            current_node = path[i]

        delta_feromon = 1.0/total_path_cost

        # feromon deposit
        current_node = path[0]
        for i in range(1, len(path)):
            graph1.feromon[current_node][path[i]] += delta_feromon
            current_node = path[i]
