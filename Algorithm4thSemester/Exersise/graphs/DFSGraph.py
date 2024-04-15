def ReadGraph(inputData, n):
    vertices = [[] for _ in range(n)]
    for edge in inputData:
        x = edge[0] - 1
        y = edge[1] - 1

        vertices[x].append(y)
        vertices[y].append(x)

    return vertices


def DFS(vertex, vertices, used):
    if used[vertex]:
        return
    used[vertex] = True
    print(vertex + 1)
    for nextVertex in vertices[vertex]:
        DFS(nextVertex, vertices, used)


def printPathWithDFS(vertices):
    vertex = 0
    used = [False] * n
    DFS(vertex, vertices, used)


inputData = [(2, 6), (1, 4), (1, 7), (2, 7),(3, 6), (3, 5), (5, 6), (3, 7)]
n = len(inputData)

vertices = ReadGraph(inputData, n)
print(vertices)
printPathWithDFS(vertices)
