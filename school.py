import string
import random
import pandas as pd


class Student:
    def __init__(self, name, math_score, eng_score):
        self.name = name
        self.math_score = math_score
        self.eng_score = eng_score

    def passingMath(self):
        return self.math_score >= 10

    def passingEng(self):
        return self.math_score >= 10

    def __str__(self):
        return f"{self.name}, Math_score: {self.math_score}, English_score: {self.eng_score}, {'--> Math Passed' if self.passingMath() else '-->Math Failed'}, {'--> Engllish Passed' if self.passingEng() else '-->English Failed'}"


class HighSchoolGrade(Student):
    def __init__(self, name, math_score, eng_score, stu_grade):
        super().__init__(name, math_score, eng_score)
        self.stu_grade = stu_grade

    def __str__(self):
        return super().__str__() + f", HighSchoolGrade: {self.stu_grade}"


class HonnorStudent(HighSchoolGrade):
    def __init__(self, name, math_score, eng_score, stu_grade, has_scholarship):
        super().__init__(name, math_score, eng_score, stu_grade)
        self.has_scholarship = has_scholarship

    def __str__(self):
        return (
            super().__str__()
            + f", Scholarship: {'Yes' if self.has_scholarship else 'No'}"
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
        rnd = random.randint(1, 2)
        if rnd == 1:
            rnd_has_scholarship = True
        else:
            rnd_has_scholarship = False
        s = HonnorStudent(
            rnd_name, rnd_math_score, rnd_eng_score, rnd_grade, rnd_has_scholarship
        )
        students.append(s)

    # with open("report.txt", "w") as file:
    for student in students:
        print(student)  # shows on screen
    # file.write(str(student) + "\n")
    print("Now students are printed based on sorted their Math scores")
    students_sorted = sorted(students, key=lambda s: s.math_score, reverse=True)
    result = list(
        map(lambda s: (s.name, s.math_score), students_sorted),
    )
    for i in result:
        print(i)
    print("Now students who has got Math score more than 16 are printed")
    high_math = list(filter(lambda s: s.math_score > 17, students_sorted))
    result = list(
        map(lambda s: (s.name, s.math_score), high_math),
    )
    for i in result:
        print(i)
    print("Now students are printed based on sorted their English scores")
    students_sorted = sorted(students, key=lambda s: s.eng_score, reverse=True)
    result = list(map(lambda s: (s.name, s.eng_score), students_sorted))
    for i in result:
        print(i)
    print("Now students who has got English score more than 16 are printed")
    high_eng = list(filter(lambda s: s.eng_score > 17, students_sorted))
    result = list(
        map(lambda s: (s.name, s.eng_score), high_math),
    )
    for i in result:
        print(i)


generate()
# with open("report.txt", "r") as f:
# print(f.read())
