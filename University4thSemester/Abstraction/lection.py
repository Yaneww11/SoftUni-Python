# procedure is void function
def print_params(**params):
    print(params)


def change_global():
    global x
    x = 3
    print(x)


print_params(name=1, type=int)
change_global()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for n in map(lambda x: 2*x, numbers):
    print(n, end=" ")
