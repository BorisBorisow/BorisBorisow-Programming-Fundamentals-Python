# numbers_str = input().split()
# numbers = []
#
# for num in numbers_str:
#     numbers.append(int(num))
#
# remover = int(input())
#
# for _ in range(remover):
#     numbers.remove(min(numbers))
#
# print(*numbers, sep=", ")

# list_of_numbers = input().split(" ")
# remover = int(input())
# sorted_list_of_numbers = [int(i) for i in list_of_numbers]
#
# for _ in range(remover):
#     sorted_list_of_numbers.remove(min(sorted_list_of_numbers))
# print("".join(str(sorted_list_of_numbers)))
#
# numbers = list(map(int, input().split()))
# removes_count = int(input())
#
# numbers_copy = numbers.copy()
# numbers_copy.sort()
# edited_list = numbers_copy[removes_count:]
# numbers = [str(x) for x in numbers if x in edited_list]
# numbers = ', '.join(numbers)
# print(numbers)


numbers = list(map(int, input().split()))
removes_count = int(input())

numbers_copy = numbers.copy()
numbers_copy.sort()
edited_list = numbers_copy[removes_count:]
numbers = [str(x) for x in numbers if x in edited_list]
numbers = ', '.join(numbers)
print(numbers)