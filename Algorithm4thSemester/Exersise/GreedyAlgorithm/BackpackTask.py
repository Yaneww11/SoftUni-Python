class MyItem:
    def __init__(self, itemNo, profit, weight):
        self.itemNo = itemNo
        self.profit = profit
        self.weight = weight
        self.ppw = 0.0


def cmp(a, b):
    return a.ppw > b.ppw


def solve(capacity, arr, n):
    for i in range(n):
        arr[i].ppw = arr[i].profit / arr[i].weight

    arr.sort(key=lambda x: x.ppw, reverse=True)

    max_profit = 0.0
    i = 0

    while capacity >= arr[i].weight and i <= n - 1:
        if capacity >= arr[i].weight:
            max_profit += arr[i].profit
            capacity -= arr[i].weight
        else:
            max_profit += capacity * arr[i].ppw
            capacity = 0
        i += 1

    return max_profit


# Example usage:
items = [MyItem(1, 60, 10), MyItem(2, 100, 20), MyItem(3, 120, 30)]
capacity = 50
n = len(items)

print("Maximum profit:", solve(capacity, items, n))
