from collections import deque


def ReadGraph(inputData, n):
    vertices = [[] for _ in range(n)]
    for edge in inputData:
        x = edge[0] - 1
        y = edge[1] - 1

        vertices[x].append(y)
        vertices[y].append(x)

    return vertices


def DFS(vertex, vertices, used, path, prefix):
    used[vertex] = True
    print(f"{prefix} {vertex + 1}")
    # With sort the order of data in input is not important, always have the same tree as e result
    for nextVertex in sorted(vertices[vertex]):
        if used[nextVertex]:
            continue
        path[nextVertex] = vertex
        DFS(nextVertex, vertices, used, path, prefix + "  ")


def printPathWithDFS(vertices, nodes):
    # Root of the result(tree)
    vertex = 2 - 1
    # List with element, if in index is true(that element is visited)
    used = [False] * (nodes + 1)
    # Path for the number
    path = [-1] * (nodes + 1)
    # The path start from vertex
    path[vertex] = -1
    print(f"Tree from DFS with root({vertex + 1})")
    DFS(vertex, vertices, used, path, "")
    print(f"{'#' * 10} End tree {'#' * 10}")
    # Print path for all
    for i in range(len(vertices)):
        print(f"{path[i] + 1} -> {i + 1}")

    # Print path from the root to number
    current = 4 - 1
    pathToCurrentNum = []
    while current != -1:
        pathToCurrentNum.append(current + 1)
        current = path[current]

    pathToCurrentNum.reverse()
    print(f"Path in tree to {pathToCurrentNum[-1]}: {' -> '.join([str(i) for i in pathToCurrentNum])}")


def printWithBFS(vertices, nodes):
    # Root of the result(tree)
    startVertex = 2 - 1
    # List with element, if in index is true(that element is visited)
    used = [False] * nodes
    used[startVertex] = True
    # Path start from the vertex
    path = [startVertex + 1]
    queue = deque()
    queue.append(startVertex)
    # List to safe distance of every element from root
    distance = [0] * nodes
    while len(queue) > 0:
        vertex = queue.popleft()
        for neighbor in vertices[vertex]:
            if used[neighbor]:
                continue
            used[neighbor] = True
            path.append(neighbor + 1)
            distance[neighbor] = distance[vertex] + 1
            queue.append(neighbor)

    print(f"Path BFS from {path[0]}: {path}")
    print(f"Distance in BFS tree from {startVertex + 1}")
    for i in range(nodes):
        print(f"{i + 1}: {distance[i]}")


def printWithDfsStack(vertices, nodes):
    # Root of the result(tree)
    startVertex = 2 - 1
    # List with element, if in index is true(that element is visited)
    used = [False] * nodes
    used[startVertex] = True
    # Path start from the vertex
    path = [startVertex + 1]
    stack = []
    stack.append(startVertex)
    # List to safe distance of every element from root
    distance = [0] * nodes
    while len(stack) > 0:
        vertex = stack.pop()
        for neighbor in vertices[vertex]:
            if used[neighbor]:
                continue
            used[neighbor] = True
            path.append(neighbor + 1)
            distance[neighbor] = distance[vertex] + 1
            stack.append(neighbor)

    print(f"Path DFS with Stack from {path[0]}: {path}")


inputData = [(2, 6), (2, 7), (1, 4), (1, 7), (3, 6), (3, 5), (5, 6), (3, 7)]
# Count nodes
n = 7
# Count edges
m = len(inputData)

vertices = ReadGraph(inputData, n)
print(vertices)
printPathWithDFS(vertices, n)
printWithBFS(vertices, n)
printWithDfsStack(vertices, n)
