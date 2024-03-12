import sys

arr = [int(i) for i in sys.argv[1:]]
unequal_numbers = []

for num in arr:
    if num in unequal_numbers:
        continue
    else:
        unequal_numbers.append(num)

else:
    print(sorted(unequal_numbers))