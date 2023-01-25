number_of_students = int(input())

students_dict = {}
count = 0

for _ in range(number_of_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(student_grade)

for key, value in students_dict.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")
