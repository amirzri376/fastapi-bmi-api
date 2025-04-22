import random
import string


class Student:
    def __init__(self, name, math_score, eng_score):
        self.name = name
        self.math_score = math_score
        self.eng_score = eng_score

    def average(self):
        return (self.math_score + self.eng_score) / 2

    def passing(self):
        return self.average() >= 10

    def show(self):
        print(
            f"Name is {self.name}, math score is  {self.math_score}, english score is {self.eng_score}, and average is {self.average()}"
        )


class HighSchoolStudent(Student):
    def __init__(self, name, math_score, eng_score, grade_level):
        super().__init__(name, math_score, eng_score)
        self.grade_level = grade_level

    def show(self):
        print(
            f"Name is {self.name}, Math score is  {self.math_score}, English score is {self.eng_score}, and average is {self.average()}, Geade_level is {self.grade_level}"
        )


def generate():
    students = []
    for i in range(10):
        rnd_name = ""
        for j in range(5):
            rnd_name += random.choice(string.ascii_lowercase)
        rnd_math_score = random.randint(1, 20)
        rnd_eng_score = random.randint(1, 20)
        rnd_grade = random.randint(1, 3)
        s = HighSchoolStudent(rnd_name, rnd_math_score, rnd_eng_score, rnd_grade)
        students.append(s)

    for student in students:
        student.show()
        if student.passing():
            print("-> Passed")
        else:
            print("-> Failed")
        print("---")
    print(f"Average over all math scores is {avg_math_score(students)}")
    print(f"Average over all english scores is {avg_eng_score(students)}")


def avg_math_score(students):
    sum = 0
    for student in students:
        sum += student.math_score
    return sum / len(students)


def avg_eng_score(students):
    sum = 0
    for student in students:
        sum += student.eng_score
    return sum / len(students)


def generate_NotC():
    students = []
    for i in range(10):
        rnd_name = ""
        for j in range(5):
            rnd_name += random.choice(string.ascii_lowercase)
        rnd_math_score = random.randint(1, 20)
        rnd_eng_score = random.randint(1, 20)
        s = rnd_name, rnd_math_score, rnd_eng_score
        students.append(s)
        avg = average(s)
        print(
            f"Name is {s[0]}, Math score is  {s[1]}, English score is {s[2]}, , and average is {avg}"
        )
        if passing(avg):
            print("-> Passed")
        else:
            print("-> Failed")
        print("---")


def average(student):
    return (student[1] + student[2]) / 2


def passing(avg):
    return avg >= 10


generate()
# generate_NotC()