import csv
from typing import Optional
from queue import PriorityQueue


class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    # use it to order in priority queue
    def __lt__(self, other):
        return self.weight < other.weight


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    # use it to order in priority queue
    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f'To node[{self.vertex}] and weight {self.weight}'


def addEdge(from_vertex, to_vertex, weight, vertices):
    vertices[from_vertex].append(Node(to_vertex, weight))


def findBestEdge(edges, tree):
    if edges.empty():
        return None
    edge = edges.get()
    vertex = edge.y if edge.x in tree else edge.x

    while vertex in tree:
        if edges.empty():
            return None
        edge = edges.get()
        vertex = edge.y if edge.x in tree else edge.x

    return edge


def FindMinimumSpanningTree(vertices, start_vertex):
    tree = set()
    sum = 0
    vertex = start_vertex
    edges = PriorityQueue()
    while True:
        tree.add(vertex)
        # add edges to edges
        for next in vertices[vertex]:
            edges.put(Edge(vertex, next.vertex, next.weight))

        # find best edge
        edge: Optional[Edge] = findBestEdge(edges, tree)

        if edge is None:
            break

        vertex = edge.y if edge.x in tree else edge.x
        sum += edge.weight

        if edges.empty():
            break
    return sum


csv_data = ("""5
8
2, 3, 3
1,3, 3
1, 2, 2
4, 5, 3
1, 4, 11
5, 2, 15
3, 4, 2
5, 3, 6""")
input_data = list(csv.reader(csv_data.splitlines()))
input_data = [[(int(value)) for value in raw] for raw in input_data]

# Number of edges
n = input_data[0][0]
# Number of vertex
m = input_data[1][0]
vertices = [[] for i in range(n + 1)]

for i in range(int(m)):
    edge = input_data[i + 2]
    addEdge(edge[0], edge[1], edge[2], vertices)
    addEdge(edge[1], edge[0], edge[2], vertices)

result = FindMinimumSpanningTree(vertices, 1)
print(result)
