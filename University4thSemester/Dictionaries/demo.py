#phonebook = {'S klasata': '0897654321', 'BMW': '0897654322'}
#print(phonebook)
#print(phonebook['BMW'])
# deepcopy - прави незавсими копия, докато copy(плитко копие) взима референцията на по сложни обекти каъо листове
# get - по - добре е да се използва, защото ако вземем не съществуващ ключ връща None
# items - връща всички елемети от речника катп списък от тюпъли(кортежи)
#print(phonebook.items())
#print(phonebook.keys())
# popitem - маха последния елемент
# setdafault - като get, но ако нямам стойноста, ще я създаде, можем да добавим и втора данна - стойност на ключа
# update - добавя елементи

#for k in phonebook:
#    print(k, phonebook[k])

# ex2
text = 'abbcdsfeeeb'
histogram = {}
for char in text:
    if histogram.get(char) is None:
        histogram[char] = 1
    else:
        histogram[char] += 1
print(histogram)

# ex1
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
value = 1
for k in my_dict:
    if my_dict[k] == value:
        print(k)