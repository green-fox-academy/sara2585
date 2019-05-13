from person import Person
class Mentor(Person):
    def __init__(self, name, age, gender, level):
        Person.__init__(self, name, age, gender)
        self.level = level
    def get_goal(self):
        print(f"Educate brilliant junior software developers.")

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender} {self.level} mentor.")

mentor = Mentor("Jane Doe", 30, "female", "intermediate")
mentor.get_goal()
mentor.introduce()


