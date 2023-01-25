# numbers = input().split(" ")
# abs_number = []
#
# for num in numbers:
#     abs_number.append(abs(float(num)))
#
# print(abs_number)

#Втори начин на решаване:
# numbers = list(map(float, input().split(" ")))
# result = [abs(num) for num in numbers]
# print(result)

# #Трети начин за решение
# def abs_numbers(nums):
#     result = [abs(num) for num in nums]
#     return result
#
# numbers = list(map(float, input().split(" ")))
# print(abs_numbers(numbers))

def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result

numbers = list(map(float, input().split(" ")))
print(abs_numbers(numbers))