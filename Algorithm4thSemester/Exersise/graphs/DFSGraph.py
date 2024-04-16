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
    for nextVertex in sorted(vertices[vertex]):
        if used[nextVertex]:
            continue
        path[nextVertex] = vertex
        DFS(nextVertex, vertices, used, path, prefix + "  ")


def printPathWithDFS(vertices):
    # Root of the result(tree)
    vertex = 2 - 1
    # List with element, if in index is true(that element is visited)
    used = [False] * n
    # Path for the number
    path = [-1] * n
    # The path start from vertex
    path[vertex] = -1
    DFS(vertex, vertices, used, path, "")
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
    print(f"Path to {pathToCurrentNum[-1]}: {' -> '.join([str(i) for i in pathToCurrentNum])}")


inputData = [(2, 6), (2, 7), (1, 4), (1, 7), (3, 6), (3, 5), (5, 6), (3, 7), ]
n = len(inputData)

vertices = ReadGraph(inputData, n)
print(vertices)
printPathWithDFS(vertices)
