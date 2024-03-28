from typing import Dict


def determinantValue(x1, y1, x2, y2, x3, y3):
    if (x1 * (y2 - y3) - y1 * (x2 - x3) + 1 * (x2 * y3 - y2 * x3)) != 0:
        return True
    return False


def countPointsMakeTriangle(point: Dict, n: int) -> int:
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if determinantValue(point[i][0], point[i][1], point[j][0], point[j][1],
                                    point[k][0], point[k][1]):
                    counter += 1

    return counter

# wor*dt 0-2 3 2
def isMask(mask, word) -> bool:
    after_mask = ""
    after_mask_length = 0
    before_mask = ""
    before_mask_mask_length = 0
    isFind = False
    for index, value in enumerate(mask):
        if value != '*':
            if not isFind:
                before_mask += value
                before_mask_mask_length += 1
            else:
                after_mask += value
                after_mask_length += 1
        else:
            isFind = True
            continue

    a = word[: before_mask_mask_length]
    b = word[len(word) - after_mask_length:]
    if a == before_mask and b == after_mask:
        return True
    return False
""""n = int(input())

dict_pointers = {}
for i in range(n):
    x = int(input())
    y = int(input())
    dict_pointers[i] = [x, y]
print(countPointsMakeTriangle(dict_pointers, n))
"""

number_masks = 2
number_words_mask = 4
for i in range(number_masks):
    mask = input("Enter the mask: ")
    for _ in range(number_words_mask):
        word = input("Enter the word: ")
        if isMask(mask, word):
            print("Yes")
        else:
            print("No")

