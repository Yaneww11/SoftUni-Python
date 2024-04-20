class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, courseSignature, nameCourse):
        self.courses[courseSignature] = nameCourse

    def getCourses(self):
        for key, value in self.courses.items():
            print(f"{key} {value}")


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, courseSignature, enrollmentYear):
        self.courses[courseSignature] = {'grades': [], 'year': enrollmentYear}

    def addGrade(self, courseSignature, grade):
        if courseSignature in self.courses:
            self.courses[courseSignature]['grades'].append(grade)

    def getCourses(self):
        for key, value in self.courses.items():
            print(f"{key} {value}")

    def getAvgGrade(self, courseSignature):
        if courseSignature in self.courses:
            return sum(self.courses[courseSignature]['grades']) / len(self.courses[courseSignature]['grades'])


t1 = Teacher('Ivan', 23, 3000)
t1.addCourse('1', 'Inf')
t1.addCourse('2', 'Inf2')
t1.getCourses()

st1 = Student('Petrov',21)
st1.attendCourse('CSCB101',2013)
st1.addGrade('CSCB101',3)
st1.addGrade('CSCB101',4)
print(st1.getAvgGrade('CSCB101'))
st1.getCourses()
