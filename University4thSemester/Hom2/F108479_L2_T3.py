import sys

arr = sys.argv[1:]
unequal_numbers = []

for num in arr:
    if num in unequal_numbers:
        print(True)
        break
    else:
        unequal_numbers.append(num)

else:
    print(False)