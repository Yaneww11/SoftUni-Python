class Employee:
    def __init__(self):
        self.workhours = 8

    def work(self):
        print(f'I work {self.workhours} hours a week')


class Manager(Employee):
    def __init__(self):
        super(Manager, self).__init__()


a = Employee()
b = Manager()
b.work()
