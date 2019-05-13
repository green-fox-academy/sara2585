from person import Person
class Student(Person):
    def __init__(self, name, age, gender, previous_organization, skipped_days = 0):
        Person.__init__(self, name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} from {self.previous_organization} who skipped {self.skipped_days} days from the course already.")

    def skip_days(self, n):
        self.skipped_days += n
        return self.skip_days

student = Student("Jane Doe", 30,"female", "The School of Life")

student.skip_days(3)
print(student.skipped_days)
student.get_goal()
