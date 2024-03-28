arr = [6, 2, 6, 2, 4, 4]
counter = 0
maxValue = 0
i = -1
while i < len(arr):
    i += 1
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            maxValue = arr[j]
            counter += arr[i] - arr[j]
            if maxValue >= arr[j + 1]:
                i = j
                break
        else:
            i = j - 1
            break

print(counter)




