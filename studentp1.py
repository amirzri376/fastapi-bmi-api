import random
import string
from tkinter.font import names
import numpy as np


def generate_stu(num_stu):
    student = []
    for i in range(num_stu):
        name = ""
        for i in range(4):
            name += random.choice(string.ascii_lowercase)
        math_score = random.randint(0, 20)
        eng_score = random.randint(0, 20)
        student.append((name, math_score, eng_score))
    print("All students with their scores (name, math score, english score)")
    for i in student:
        print(i)
    return student


def is_palindrome(list, num):
    print("palindrome function is running!")
    checker = False
    for i in range(num):
        name = list[i][0]
        if name[0] == name[-1]:
            print(f"{name} is palindrome")
            checker = True
    if checker == False:
        print("There is no palindrome")


def statistics(list, num):
    print("statistics function is running!")
    math_scores = []
    max_math_score_names = []
    eng_scores = []
    max_eng_score_names = []
    for i in range(num):
        math_scores.append(list[i][1])
        eng_scores.append(list[i][2])
    max_math_score = max(math_scores)
    max_eng_score = max(eng_scores)
    avg_math_score = sum(math_scores) / num
    avg_eng_score = sum(eng_scores) / num
    print(f"average of math secores are :  {avg_math_score}")
    print(f"average of english secores are :  {avg_eng_score}")
    for i in range(num):
        if list[i][1] == max_math_score:
            max_math_score_names.append(list[i][0])
    print(f"{max_math_score_names} have got the maxinum {max_math_score} score in math")
    for i in range(num):
        if list[i][2] == max_eng_score:
            max_eng_score_names.append(list[i][0])
    print(
        f"{max_eng_score_names} have got the maxinum {max_eng_score} score in english"
    )


def passing(list, num):
    pass_math = []
    pass_eng = []
    for i in range(len(list)):
        if list[i][1] > 9:
            pass_math.append(list[i][0])
    print(f"{pass_math} have passed the math course")
    for i in range(len(list)):
        if list[i][2] > 9:
            pass_eng.append(list[i][0])
    print(f"{pass_eng} have passed the english course")


num_stu = int(input("How many student: "))
data = generate_stu(num_stu)
is_palindrome(data, num_stu)
statistics(data, num_stu)
passing(data, num_stu)