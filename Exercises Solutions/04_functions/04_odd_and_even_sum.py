# def odd_and_even_nums(some_string):
#     odd_sum = 0
#     even_sum = 0
#     for current_num in some_string:
#         if current_num % 2 != 0:
#             odd_sum += current_num
#         else:
#             even_sum += current_num
#     return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
#
#
# odd_even_string = [int(i) for i in input()]
# print(odd_and_even_nums(odd_even_string))

def odd_even_sum(some_string):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for current_num in some_string:
        if int(current_num) % 2 != 0:
            sum_of_odd_digits += int(current_num)
        else:
            sum_of_even_digits += int(current_num)

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

string_of_numbers = input()
print(odd_even_sum(string_of_numbers))