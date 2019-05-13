class Student():
    def __init__(self, name):
        self.name = name
    def learn(self):
        return "how to read..."
    def question(self, Teacher):

        return Teacher.answer("ans")


class Teacher():
    def __init___(self, name):
        self.name = name

    def teach(self, Student):
        return Student.learn()

    def answer(self, ans):
        return "the answer is A "
        
A = Student("A")
B = Teacher()
print(A.question(B))
print(B.teach(A))
