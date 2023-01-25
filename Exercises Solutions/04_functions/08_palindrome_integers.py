
def palindrome(list_of_integers):
    for current_int in list_of_integers:
        palindrome = []
        if current_int == current_int[::-1]:
            palindrome += [current_int]
        print(bool(palindrome))

numbers = input().split(", ")
palindrome(numbers)


#second variant
# def palindrome(number):
#     return number == number[::-1]
#
#
# input_numbers = input().split(", ")
#
#
# for number in input_numbers:
#     print(palindrome(number))


#Third variant
# def palindrome_integer(list_of_integers):
#     for integer in list_of_integers:
#         integer = list(integer)
#         palindrome = integer[:] == integer[::-1]
#         print(palindrome)
#
#
# numbers = list(input().split(', '))
# palindrome_integer(numbers)