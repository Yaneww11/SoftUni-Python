def searchFibonacci(num, calculateNumbers):
    if num == 0:
        return 0
    elif num == 1:
        calculateNumbers[1] = 1
        return 1
    else:
        if num in calculateNumbers:
            return calculateNumbers[num]
        else:
            calculateNumbers[num] = (searchFibonacci(num - 1, calculateNumbers) +
                                     searchFibonacci(num - 2, calculateNumbers))
            return calculateNumbers[num]


def sliceArray(start, end):
    return array[start - 1:end]


stat = int(input("Enter a index of start num: "))
end = int(input("Enter a index of end num: "))
array = [0] * (end + 1)
searchFibonacci(end, array)
print(sliceArray(stat, end))
