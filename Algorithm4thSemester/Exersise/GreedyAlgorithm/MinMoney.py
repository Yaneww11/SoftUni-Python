import math

banknoteValues = [0.01, 0.05, 0.1, 0.5, 1]
n = len(banknoteValues)

remainder = 1.52
coinsRemainder = []
index = n - 1
while remainder != 0:
    currentValue = banknoteValues[index]
    if remainder - currentValue >= 0:
        remainder = round(remainder - currentValue, 2)
        coinsRemainder.append(currentValue)
    else:
        index -= 1

print(coinsRemainder)