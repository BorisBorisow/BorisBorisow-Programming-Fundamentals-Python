def calculations_func(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return int(a / b)
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b


type_of_operation = input()
first_num = int(input())
second_num = int(input())
print(calculations_func(first_num, second_num, type_of_operation))


# def calculator(num1, num2, operator):
#     calc_dict = {
#         'add': lambda x, y: x + y,
#         'subtract': lambda x, y: x - y,
#         'multiply': lambda x, y: x * y,
#         'divide': lambda x, y: x / y
#     }
#
#     return calc_dict[operator](num1, num2)
#
#
# a = int(input())
# b = int(input())
# operator_input = input()
#
# print(calculator(a, b, operator_input))
