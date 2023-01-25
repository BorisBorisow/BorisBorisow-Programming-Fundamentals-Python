def sum_numbers(first, second):
    return first + second


def subtract(sum, third):
    return sum - third


def sum_and_subtract_numbers(first, second, third):
    sum_first_second = sum_numbers(first, second)
    result = sum_first_second - third
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(sum_and_subtract_numbers(first_num, second_num, third_num))
