class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __next__(self):
        if self.b == 0:
            self.b = 1
            return 0
        self.c = self.a + self.b
        self.a = self.b
        self.b = self.c
        return self.a

    def __iter__(self):
        return self


fib = Fibs()
for i in fib:
    if i > 100:
        break
    print(i)
