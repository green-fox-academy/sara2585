from person import Person
class Sponsor(Person):
    def __init__(self, name, age, gender, company, hired_students):
        Person.__init__(self, name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} who represents {self.company} and hired {self.hired_students} students so far.")

    def hire(self):
        self.hired_students += 1
        return self.hired_students

    def get_goal(self):
        print("Hire brilliant junior software developers.")

sponsor = Sponsor("Jane Doe", 30, "female", "Google", 0)
sponsor.introduce()
print(sponsor.hire())
sponsor.get_goal()
