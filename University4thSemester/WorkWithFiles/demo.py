# ex 1
lines = []
f = open('somefile.txt', 'r')
for line in f:
    lines.append(line)

f.close()

lines[-1] += '\n'
lines = sorted(lines)
lines[-1] = lines[-1].strip('\n')

f = open('somefile.txt', 'w')
f.writelines(lines)
f.close()

# ex 2
my_dict = {}
for line in open('stemA.txt'):
    word, root = line.split(':')
    root = root.strip('\n')
    if word not in my_dict:
        my_dict[word] = root

word = 'auricer'
print(my_dict.get(word))
