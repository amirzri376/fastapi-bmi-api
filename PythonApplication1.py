import string
import random
import pandas as pd
import numpy as np


def BmiCal():
    weight = float(input("Enter Weight (kg): "))
    height = float(input("Enter Height (m) : "))
    bmi = weight / (height * 2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("Normal")
    elif 24.9 < bmi <= 30:
        print("Overweight")
    else:
        print("Obese")


def AvgGrade():
    grades = []
    for i in range(5):
        grades.append(int(input(f"Enter a gradeunmber {i} from 0 to 100 : ")))
    avgG = sum(grades) / 5
    if avgG >= 90:
        print("Excelent")
    elif 50 <= avgG < 90:
        print("Good")
    else:
        print("Horrible")


def GuessRandNum():
    rndNum = random.randint(1, 10)

    while True:
        userNum = int(input("Enter an integer Number: "))
        if userNum == rndNum:
            break
        else:
            continue
    print("You got it!!")


def MaxMinLarger():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 100))
    max_num = max(numbers)
    min_num = min(numbers)
    lnumbers = []
    for j in range(len(numbers)):
        if numbers[j] > 20:
            lnumbers.append(numbers[j])
    print(f"numbers are {numbers}")
    print(f"max is {max_num}")
    print(f"min is {min_num}")
    print(f"Larger than 20 are {lnumbers}")


def tupleexp1():
    numbers = ()  # Start with an empty tuple
    for i in range(10):
        numbers += (random.randint(1, 10),)  # Concatenate a 1-element tuple


def tupleexp2():
    result = ()
    for i in range(10):
        num = random.randint(0, 100)
        rand_str = ""
        for j in range(5):
            rand_str += random.choice(string.ascii_lowercase)
        result += ((num, rand_str),)
    for i in result:
        print(i)


def listexp1():
    result = []
    for i in range(10):
        num = random.randint(0, 100)
        rand_str = ""
        for j in range(5):
            rand_str += random.choice(string.ascii_lowercase)
        result.append((num, rand_str))
    for i in result:
        print(i)


def compTriple():
    result = ()
    for j in range(10):
        name_rnd = ""
        math_score = random.randint(0, 20)
        english_score = random.randint(0, 20)
        for i in range(5):
            name_rnd += random.choice(string.ascii_lowercase)
        result += ((name_rnd, math_score, english_score),)
    name_rnd = []
    name_max, math_max, english_max = result[0]
    for i in result:
        name_rnd, math_score, english_score = i
        temp_math_max = math_score
        temp_english_max = english_score
        if math_max <= temp_math_max:
            math_max = temp_math_max
            name_math_max = name_rnd
        if english_max <= temp_english_max:
            english_max = temp_english_max
            name_english_max = name_rnd
        print(
            f"name : {name_rnd}, math_score = {math_score}, english_score = {english_score}"
        )
    print(
        f"math_max = {math_max} from {name_math_max}, english_max = {english_max} from {name_english_max}"
    )


def max3num(a, b, c):
    x = a
    y = b
    z = c
    maxi = a
    if b > a:
        maxi = b
        a = b
    if c > a:
        maxi = c
    print(f"a = {x}, b = {y}, c = {z}")
    print(f"maximum is {maxi}")


def palindrome(word):
    if word[0] == word[-1]:
        print("true")
        return True
    else:
        print("false")
        return False


def matrix():
    matrix = []

    # Add one row at a time
    row1 = [1, 2, 3]
    row2 = [4, 5, 6]

    matrix.append(row1)
    matrix.append(row2)
    print(matrix[0])
    print(matrix[1])


def funListNumpy():
    matrix1 = []
    raw11 = []
    raw12 = []
    for i in range(1, 4):
        raw11.append(random.randint(1, 4))
        raw12.append(random.randint(1, 4))
    matrix1.append(raw11)
    matrix1.append(raw12)
    print("this is the first matrix")
    for i in matrix1:
        print(i)

    matrix2 = []
    raw21 = []
    raw22 = []
    for i in range(1, 4):
        raw21.append(random.randint(1, 4))
        raw22.append(random.randint(1, 4))
    matrix2.append(raw21)
    matrix2.append(raw22)
    print("this is the second matrix")
    for i in matrix2:
        print(i)
    A = np.array(matrix1)
    B = np.array(matrix2)
    print("this is their multiplication")
    print(A * B)


def sortexp():
    students = []
    for i in range(10):
        stu_name = ""
        for j in range(5):
            stu_name += random.choice(string.ascii_lowercase)
        math_score = random.randint(0, 20)
        students.append((stu_name, math_score))
    for i in students:
        print(i)
    print("Let us print students based on scores")
    sorted_students = sorted(students, key=lambda s: s[1])
    for i in sorted_students:
        print(i)


def listmapsortfilter():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 10))
    print("All numbers are: ", numbers)
    result = list(filter(lambda s: s % 2 == 0, numbers))
    print("Even numbers are:", result)

    result = list(map(lambda s: s * s, numbers))
    print("Squared of numbers are:", result)

    words = []
    for i in range(20):
        rnd_str = ""
        for i in range(5):
            rnd_str += random.choice(string.ascii_lowercase)
        words.append(rnd_str)

    print("All words are: ", words)
    result = list(filter(lambda s: s[0] in ("a", "b", "c"), words))
    print("words start with (a,b):", result)


def compreexp():
    nums = []
    for i in range(10):
        nums.append(random.randint(0, 100))

    print("Numbers are: ", nums)
    squared_nums = [x * x for x in nums]
    print("Suqred_numbers are : ", squared_nums)
    even = [x for x in nums if x % 2 == 0]
    print("Even_numbers are : ", even)


def pandasexp():
    data = {
        "Name": ["Amir", "Sara", "Ali", "Nina", "Omar"],
        "Math": [15, 18, 12, 19, 16],
        "English": [17, 16, 13, 20, 14],
    }
    df = pd.DataFrame(data)
    df["Average"] = (df["Math"] + df["English"]) / 2
    df["P&F"] = np.where(df["Average"] >= 16, "Passed", "Failed")
    print(df)
    high_average = df[df["Average"] >= 16]
    print(high_average)
    sorted_df = df.sort_values(by="English", ascending=False)
    print(sorted_df)
    passed_students = df[df["P&F"] == "Passed"][["Name", "Average"]]
    print(passed_students)
    passed_students.to_csv("passed_students.csv", index=False)


pandasexp()
# compreexp()
# sortexp()
# funListNumpy()
# matrix()
# BmiCal()
# AvgGrade()
# GuessRandNum()
# MaxMinLarger()
# tupleexp1()
# tupleexp2()
# listexp1()
# compTriple()
# for i in range(3):
# for j in range(3):
# for k in range(3):
# max3num(i, j, k)
# palindrome("amir")
# listmapsortfilter()