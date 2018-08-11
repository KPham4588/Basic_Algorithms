from collections import defaultdict

class Graph:

    def __init__(self):
        pass

    graph = {'A': {'B', 'C'},
             'B': {'D', 'E'},
             'C': {'F', 'G'},
             'D': {'H'},
             'E': set(),
             'F': set(),
             'G': set('I'),
             'H': set(),
             'I': set()}