class Zombie:
    members = 0

    def __init__(self, name):
        self.name = name

    def sayYourName(self):
        print("Aaargh, ", self.name)

    @staticmethod
    def summon():
        Zombie.members += 1


z1 = Zombie("Mariicho")
z1.summon()
print(Zombie.members)
z2 = Zombie("Ivanka")
z2.summon()
print(Zombie.members)


class Human:
    def __init__(self, name):
        self.name = name

    def sayYourName(self):
        print("Hello, I am ", self.name)


class Zombie(Human):
    def sayYourName(self):
        print("Aaargh , ", self.name)


# __init__ method is inherited
h1 = Human("Mariicho")
h1.sayYourName()
z1 = Zombie("Ivanka")
z1.sayYourName()
