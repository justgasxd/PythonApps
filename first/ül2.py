# ülesanne 10


num_grades = int(input('Mitu hinnet soovite sisestada? '))

grades = []

# Loop to get each grade
for i in range(num_grades):
    grade = float(input(f'Sisestage hinne {i + 1}: '))
    grades.append(grade)

average = sum(grades) / len(grades)

print(f'Keskmine hinne on: {average:.2f}')