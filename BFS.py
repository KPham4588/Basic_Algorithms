# sample BFS with a queue
# the graph is implemented as a dictionary with a set of nodes to each key (which itself is a parent node)
from Graph import Graph


def breadth_first_search(graph, start):

    # make a set of visited nodes as well as a queue to keep track of
    # the order of nodes to be visited
    visited = set()
    queue = []
    queue2 = []

    queue.extend(start)
    queue2.extend(start)

    # while queue is not empty, we have nodes to explore
    while queue:

        # take the first node from the queue and mark as visited
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)

        # iterate over the neighbors of said node and visit all "new" ones
        for neighbor in (graph[node] - visited):
            if neighbor not in visited:
                queue.extend(neighbor)
                queue2.extend(neighbor)
                visited.add(neighbor)
    print("BFS: ")
    print(queue2)


breadth_first_search(Graph.graph, 'A')
