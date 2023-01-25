def is_perfect(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect(number))

#Second option
# def perfect_number(number: int):
#     result = sum(n for n in range(1, number) if number % n == 0)
#     if result == number:
#         return 'We have a perfect number!'
#     return "It's not so perfect."
#
#
# num = int(input())
# print(perfect_number(num))
