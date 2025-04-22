
import random
import string
import numpy as np


class Student:
    def __init__(self, name, math_score, english_score):
        self.name = name
        self.math_score = math_score
        self.english_score = english_score

    def average(self):
        return (self.math_score + self.english_score) / 2

    def show(self):
        print(f"{self.name}, Math = {self.math_score}, English = {self.english_score} ")


class Rectangle:
    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def show(self):
        print(f"Width = {self.width}, Height = {self.height}")
        print(f"Area  = {self.area()}")
        print(f"Perimeter = {self.perimeter}")


r1 = Rectangle(4, 5)
r1.show()