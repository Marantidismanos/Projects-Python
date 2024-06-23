student_score = {
    "Harry": 81,
    "Ron":78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for key in student_score:
    if student_score[key]<=70:
        print(f" '{key}': 'Fail' ")
    elif student_score[key]>=71 and student_score[key]<=80:
        print(f" '{key}': 'Acceptable' ")
    elif student_score[key]>=81 and student_score[key]<=90:
        print(f" '{key}': 'Exceeds Expectations' ")
    elif student_score[key]>=91 and student_score[key]<=100:
        print(f" '{key}': 'Outstanding' ")
