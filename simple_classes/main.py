# main.py
from Student import Student
from Rectangle import *

student1 = Student('Reimo', 16) # objekti loomine
student1.show_info()
print(student1.name) # Ainult nimi
print(student1.age) # ainult vanus
student1.name = 'Mari'
student1.age = 99
student1.show_info()

for x in range(3):
    student1.birthday()

student1.show_info()

print('----')
rectangle = Rectangle(5, 10)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.diagonaal())