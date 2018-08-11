# BFS and DFS only differs significantly in its process;
# in implementation the difference is simply that BFS uses a queue and DFS a stack
from Graph import Graph


def depth_first_search(graph, start):

    # make a stack instead of a queue
    # to keep track of nodes
    visited = set()
    stack = []
    stack2 = []

    stack.extend(start)
    stack2.extend(start)

    # while stack is not empty, there are nodes to explore
    while stack:

        # take the last node from the stack and mark as visited
        node = stack.pop()
        if node not in visited:
            visited.add(node)

        # iterate over neighbors and add new, unvisited nodes to stack
        for neighbor in (graph[node] - visited):
            if neighbor not in visited:
                stack.extend(neighbor)
                stack2.extend(neighbor)
                visited.add(neighbor)
    print("DFS:\n", stack2)


depth_first_search(Graph.graph, 'A')
