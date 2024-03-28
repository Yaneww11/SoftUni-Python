
def min_square(N):
    DP = []
    for i in range(N):
        DP.append(i)


    a = []
    for i in range(N):
        if i * i <= N:
            a.append(i * i)
        else:
            break

    m = len(a)
    for i in range(1, N):
        for j in range(m):
            if i >= a[j] and DP[i - a[j] + 1 < DP[i]]:
                DP[i] = DP[i - a[j]] + 1

    return DP[i]


N = int(input())
print(min_square(N))