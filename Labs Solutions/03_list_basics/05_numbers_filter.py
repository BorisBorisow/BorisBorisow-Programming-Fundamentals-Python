n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
numbers = []
filtered = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

for num in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
    )
    if filtered_command:
        filtered.append(num)

print(filtered)



# n = int(input())
# list_numbers = []
# filtered_list = []
#
# for x in range(n):
#     number = int(input())
#     list_numbers.append(number)
#
# command = input()
# if command == "even":
#     filtered_list = [el for el in list_numbers if el % 2 == 0]
# elif command == "odd":
#     filtered_list = [el for el in list_numbers if el % 2 != 0]
# elif command == "positive":
#     filtered_list = [el for el in list_numbers if el > 0]
# elif command == "negative":
#     filtered_list = [el for el in list_numbers if el < 0]
# print(filtered_list)


