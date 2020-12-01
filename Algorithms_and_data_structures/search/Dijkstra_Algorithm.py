infinity = float("inf")


start = "a"
finish = "f"


graph = {}

graph["a"] = {}
graph["a"]["b"] = 10

graph["b"] = {}
graph["b"]["c"] = 20

graph["c"] = {}

graph["c"]["f"] = 30
graph["c"]["d"] = 1

graph["d"] = {}
graph["d"]["b"] = 1

graph["f"] = {}


costs = {}
for i in graph[start]:
    costs[i] = graph[start][i]
for i in graph.keys():
    if i != start and i not in costs.keys():
        costs[i] = infinity
#print(costs)

parents = {}
for i in graph[start]:
    parents[i] = start
parents[finish] = None
#print(parents)

processed = set()


def find_lowest_cost_node(costs):
    """
    Находит узел с наименьшей стоимостью
    """
    global processed
    lowestC = infinity
    lowestA = None
    for i in costs.keys():
        if costs[i] < lowestC and i not in processed:
            lowestC = costs[i]
            lowestA = i
    return lowestA


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)

print(costs)


