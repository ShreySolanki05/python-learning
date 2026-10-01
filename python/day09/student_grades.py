class Student:
    def __init__(self, name):
        self.name = name 
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def average(self):
        return sum(self.grades)/len(self.grades)

s1 = Student("ss")
s1.add_grade(70)
s1.add_grade(65)
s1.add_grade(90)
s1.add_grade(80)
print(s1.average())