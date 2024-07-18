grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()

grades_average = [sum(grades[0]) / len(grades[0]),
                  sum(grades[1]) / len(grades[1]),
                  sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]),
                  sum(grades[4]) / len(grades[4]),]

dict_grades_1 = dict(zip(students, grades_average))\

dict_grades_2 = dict(zip(students, list(map(lambda x: sum(x) / len(x), grades))))

print(dict_grades_1)
print(dict_grades_2)