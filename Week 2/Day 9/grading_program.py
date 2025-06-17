student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def get_grade(score: int):
    if score > 90:
        return str("Outstanding")
    elif score > 80:
        return str("Exceeds Expectations")
    elif score > 70:
        return str("Acceptable")
    else:
        return str("Fail")

def change_score(student_scores: dict[str, int]):
    student_grades = {}
    for student in student_scores:
        grade = get_grade(int(student_scores[student]))
        student_grades[student] = grade
    return student_grades

student_grades = change_score(student_scores)
print(student_grades)