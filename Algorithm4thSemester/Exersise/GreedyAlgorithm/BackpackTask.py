class MyItem:
    def __init__(self, item_no, profit, weight, ppw=0):
        self.item_no = item_no
        self.profit = profit
        self.weight = weight
        self.ppw = ppw


def cmp(a, b):
    return a.ppw > b.ppw


def fractional_backpack(capacity, arr):
    for item in arr:
        item.ppw = item.profit / item.weight

    arr.sort(key=lambda x: x.ppw, reverse=True)

    max_profit = 0.0
    for item in arr:
        if capacity >= item.weight:
            max_profit += item.profit
            capacity -= item.weight
        else:
            max_profit += capacity * item.ppw
            capacity = 0
            break

    return max_profit


c = 25
arr = [MyItem(1, 30, 10), MyItem(2, 20, 5), MyItem(3, 40, 15), MyItem(4, 36, 8)]

print("Result:", fractional_backpack(c, arr))
