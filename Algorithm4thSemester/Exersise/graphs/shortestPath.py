import heapq
import sys
from typing import List, Optional, Set


class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

    # use it to order in priority queue
    def __lt__(self, other):
        return self.weight < other.weight

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
    numberVertex = len(vertices)
    distancesFromStart: list[int] = [sys.maxsize] * (numberVertex - 1)
    distancesFromStart[0] = 0
    used: Set = set()

    # Use priority queue, to get min element in every pop
    queue = []
    heapq.heappush(queue, Node(start, 0))

    # repeat
    for i in range(numberVertex):
        # find best element(min)
        node: Node = heapq.heappop(queue)
        while queue and node.vertex in used:
            node = heapq.heappop(queue)
        used.add(node.vertex)

        # update distance
        nextNode: Node
        for nextNode in vertices[node.vertex]:
            currentDistance = distancesFromStart[nextNode.vertex]
            newDistance = distancesFromStart[node.vertex] + nextNode.weight
            if currentDistance > newDistance:
                distancesFromStart[nextNode.vertex] = newDistance
                heapq.heappush(queue, Node(nextNode.vertex, newDistance))

    return distancesFromStart


inputData1 = [(1, 2, 2), (1, 3, 3), (1, 4, 11), (2, 3, 3), (2, 5, 15), (3, 4, 2), (3, 5, 6), (4, 5, 3)]
# Number of nodes
n = 5
# Number of edges
m = 8
vertices = ReadWeightedGraph(inputData1, n)
print(vertices)
distances = Dijkstra(vertices, 0)
print(" ".join([str(x) for x in distances]))