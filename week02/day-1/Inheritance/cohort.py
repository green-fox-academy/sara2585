from mentor import Mentor
from student import Student

class Cohort():
    def __init__(self, name):
        self.name = name
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)
        return self.students
    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)
        return self.mentors

    def info(self):
        print(f"The {self.name} cohort has {len(self.students)} students and {len(self.mentors)} mentors.")

    
#ss = Student("Sara", 20, "female", "Test")
#cor = Cohort("test")
#cor.add_students(ss)
#print(cor.add_students(ss))


        
