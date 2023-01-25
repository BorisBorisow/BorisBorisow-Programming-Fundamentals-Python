#
#
# def type_of_grade(grade):
#     if 2.00 <= grade <= 2.99:
#         result = "Fail"
#     elif 3.00 <= grade <= 3.49:
#         result = "Poor"
#     elif 3.50 <= grade <= 4.49:
#         result = "Good"
#     elif 4.50 <= grade <= 5.49:
#         result = "Very Good"
#     elif 5.50 <= grade <= 6.00:
#         result = "Excellent"
#
#     return result
#
# score = float(input())
# print(type_of_grade(score))

def grades(grade):
    current_grade = ""
    if grade <= 2.99:
        current_grade = "Fail"
    elif grade >= 3.00 and grade <= 3.49:
        current_grade = "Poor"
    elif grade >= 3.50 and grade <= 4.49:
        current_grade = "Good"
    elif grade >= 4.50 and grade <= 5.49:
        current_grade = "Very Good"
    elif grade >= 5.50 and grade <= 6.00:
        current_grade = "Excellent"

    return current_grade


grade = float(input())
print(grades(grade))