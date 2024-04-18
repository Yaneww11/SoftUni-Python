from collections import deque


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'To node[{self.vertex}] - weight {self.weight}'


def addEdge(vertices, fromm, to, weight):
    vertices[fromm].append(Node(to, weight))


def ReadWeightedGraph(data, nodes):
    vertices = [[] for _ in range(nodes + 1)]
    for edge in data:
        addEdge(vertices, edge[0] - 1, edge[1] - 1, edge[2])
        addEdge(vertices, edge[1] - 1, edge[0] - 1, edge[2])

    return vertices


def Dijkstra(vertices, start):
    queue = deque()


inputData1 = [(1, 2, 2), (1, 3, 3), (1, 4, 11), (2, 3, 3), (2, 5, 15), (3, 4, 2), (3, 5, 6), (4, 5, 3)]
# Number of nodes
n = 5
# Number of edges
m = 8
vertices = ReadWeightedGraph(inputData1, n)
print(vertices)
Dijkstra(vertices, 0)
