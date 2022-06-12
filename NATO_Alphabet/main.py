# numbers = [1, 2, 3]
# new_numbers = [y + 1 for y in numbers]
# print(new_numbers)
#
# name = "zhanma"
# new_name = [x for x in name]
# print(new_name)
#
# aaa = ['alex', 'beth', 'cathy', 'david']
# new_aaa1 = [bbb1 for bbb1 in aaa if len(bbb1) == 4]
# new_aaa2 = [bbb2.upper() for bbb2 in aaa]
# print(new_aaa1)
# print(new_aaa2)
#
# import random
#
# students = ['alex', 'beth', 'cathy', 'david']
# students_scores = {student: random.randint(0, 100) for student in students}
# print(students_scores)
#
# passed_stu = {student: score for (student, score) in students_scores.items() if score > 60}
# print(passed_stu)

import pandas
import csv

data = pandas.read_csv("nato_phonetic_alphabet.csv")

print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(phonetic_dict)

word = input("Enter a word:").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)