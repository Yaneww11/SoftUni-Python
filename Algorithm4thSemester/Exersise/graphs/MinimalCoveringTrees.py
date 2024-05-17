import csv
from typing import Optional, List
from queue import PriorityQueue


class Edge:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

    # use it to order in priority queue
    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f'{self.x} -> {self.y} ({self.weight})'


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    # use it to order in priority queue
    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f'To {self.vertex} ({self.weight})'


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
    # sum = 0
    mst: List[Edge] = []
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
        mst.append(edge)
        # sum += edge.weight

        if edges.empty():
            break
    # return sum
    return mst


def FindMinimumSpanningTreeWhichIncludeEdge(vertices, fromVertex, toVertex, weightEdge):
    tree = set()
    tree.add(fromVertex)
    tree.add(toVertex)
    # sum = 0
    mst: List[Edge] = [Edge(fromVertex, toVertex, weightEdge)]
    vertex = fromVertex
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
        mst.append(edge)
        # sum += edge.weight

        if edges.empty():
            break
    # return sum
    return mst


csv_data = ("""5
8
1,3, 3
1, 2, 2
4, 5, 3
1, 4, 11
5, 2, 15
3, 4, 2
5, 3, 6
2, 3, 3""")
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

mst = FindMinimumSpanningTree(vertices, 1)
sum_mst_path = sum([mst[i].weight for i in range(len(mst))])
print('\n'.join(str(x) for x in mst))
print(f'The sum is {sum_mst_path}')
print()

startEdge = Edge(1, 4, 11)
print(f"Tree which start from Edge({startEdge.x}, {startEdge.y}, {startEdge.weight})")
mst2 = FindMinimumSpanningTreeWhichIncludeEdge(vertices, startEdge.x, startEdge.y, startEdge.weight)
sum_mst_path = sum([edge.weight for edge in mst2])
print('\n'.join(str(x) for x in mst2))
print(f'The sum is {sum_mst_path}')
