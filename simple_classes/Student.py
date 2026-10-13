# Student.py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'{self.name}, {self.age} aastat.')

    def birthday(self):
        self.age += 1