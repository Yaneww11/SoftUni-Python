beforeMedium = -1


def searchNum(arr, start, end, num: int):
    global beforeMedium
    medium = round((end + start) / 2)
    if arr[medium] == num:
        return f"Fund {num} in index {medium}"
    if beforeMedium == medium:
        return f"Not found {num}"
    elif arr[medium] > num:
        beforeMedium = medium
        return searchNum(arr, start, medium - 1, num)
    elif arr[medium] < num:
        beforeMedium = medium
        return searchNum(arr, medium + 1, end, num)


arr = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195, 202, 205, 212, 248, 249, 256, 263, 272, 288, 289,
       290, 296, 332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444, 486, 493, 497, 499, 510, 513, 514, 519,
       521, 521, 535, 546, 552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692, 711, 713, 731, 739, 740, 842,
       858, 885, 887, 888, 893, 898, 900, 903, 908, 909, 959, 988]


print(searchNum(arr, 0, len(arr), 63))
