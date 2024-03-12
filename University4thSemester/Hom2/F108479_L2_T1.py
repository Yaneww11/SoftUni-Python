import sys

arr = sys.argv[1:]
if all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
    print("sorted")
else:
    print("unsorted")


