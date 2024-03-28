arr = [5, 33, 20, 35, 35, 45]
maxElement = arr[0]
counter = 0


def heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heapSort(arr, n):
    for i in range(n / 2 - 1, -1, -1):
        heap(arr, i, n - 1)

    for i in range(n - 1, -1, -1):
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
        heap(arr, n, 0)

    return arr


n = 5
arr = [5, 33, 20, 35, 35]
print(heapSort(arr, n))
