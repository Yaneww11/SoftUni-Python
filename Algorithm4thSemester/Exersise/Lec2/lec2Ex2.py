def solve(n):
    if n == 0 or n == 1:
        return n
    DP = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        p = DP[i // 4] + DP[i // 2] + DP[i // 3]
        if i > p:
            DP[i] = i
        else:
            DP[i] = p

    return DP[n]


def find_length(arr, n):
    up = []
    down = []
    for i in range(n):
        up.append(1)
        down.append(1)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                up[i] = max(up[i], down[j] + 1)
            elif arr[i] < arr[j]:
                down[i] = max(down[i], up[j] + 1)

    m = 0
    for i in range(n):
        m = max(m, max(up[i], down[i]))

    return m


def find_length_subst(arr1, n1, arr2, n2, arr3, n3):
    min_length = min(n1, n2, n3)
    DP = [0 for i in range(min_length)]
    print(DP)



print(solve(2))

n = 10
arr = [5, 2, 4, 1, 6, 3, 8, 9, 10, 11]
print(find_length(arr, n))
