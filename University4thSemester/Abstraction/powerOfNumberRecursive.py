def pow(num, power):
    if power == 1:
        return num
    else:
        return num * pow(num, power - 1)


print(pow(2, 10))
