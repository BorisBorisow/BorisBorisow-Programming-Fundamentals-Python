def smallest_number(some_numbers):
    return min(some_numbers)

first_num = int(input())
second_num = int(input())
third_num = int(input())
all_numbers = [first_num, second_num, third_num]
min_number = smallest_number(all_numbers)
print(min_number)