def createMaze(matrix, countRow, countColum, purposeX, purposeY):
    for i in range(countRow):
        matrix.append([])
        for j in range(countColum):
            if i == 0 or j == 0 or j == countColum - 1 or i == countRow - 1:
                matrix[i].append('#')
            elif i == 2 and j < 9:
                matrix[i].append('#')
            elif i == 4 and 2 < j < 8:
                matrix[i].append('#')
            elif 1 < i < 5 and (j == 9 or j == 2):
                matrix[i].append('#')
            elif i == purposeY and j == purposeX:
                matrix[i].append('g')
            else:
                matrix[i].append(' ')


def printMaze(matrix, countRow):
    for i in range(countRow):
        print(' '.join(str(x) for x in matrix[i]))


def createPath(maze, x, y, row, col, symbol='.'):
    if x < 0 or x >= row or y < 0 or y >= col:
        return
    if maze[x][y] == 'g':
        isSearchPurpose = True
        printMaze(maze, row)

    if maze[x][y] != ' ':
        return

    maze[x][y] = symbol
    createPath(maze, x, y + 1, row, col, symbol)  # top
    createPath(maze, x, y - 1, row, col, symbol)  # bottom
    createPath(maze, x - 1, y, row, col, symbol)  # left
    createPath(maze, x + 1, y, row, col, symbol)  # right
    maze[x][y] = 'X'


maze = []
# Row of the display
m = 7

# Column of the display
n = 12

# Coordinate provided by the user
x = 3
y = 3

createMaze(maze, m, n, x, y)
printMaze(maze, m)
print("      THE PATH IS")
createPath(maze, 1, 1, m, n)
