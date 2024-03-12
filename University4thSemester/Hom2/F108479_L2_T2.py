import sys

arr = sys.argv[1:]

str1 = sorted(list(arr[0].lower()))
str2 = sorted(list(arr[1].lower()))

if str1 == str2:
    print("True")
else:
    print("False")