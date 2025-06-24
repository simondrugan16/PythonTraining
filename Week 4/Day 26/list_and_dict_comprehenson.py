import random
import pandas

name = "simon"

new_list = [letter for letter in name]

print(new_list)

double_ranged = [num * 2 for num in range(1, 5)]

print(double_ranged)

conditional_comprehension = [num * 10 for num in range(1, 10) if num % 2 == 0]

print(conditional_comprehension)

list_of_ppl = ["me", "you", "him", "her", "them"]

student_scores = {student:random.randint(1, 100) for student in list_of_ppl}

print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}

print(passed_students)

student_dict = {
    "student": ["me", "you", "they"],
    "scores": [19, 59, 99]
}
student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student)