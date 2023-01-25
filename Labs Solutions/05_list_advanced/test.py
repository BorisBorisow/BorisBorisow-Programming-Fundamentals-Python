# import timeit
#
# def even_numbers_with_comprehension():
#     return [num for num in [1, 2, 3, 4, 5, 6]]
#
# def even_numbers_with_loop():
#     even_nums = []
#
#     for num in [1, 2, 3, 4, 5, 6]:
#         even_nums.append(num)
#
#     return even_nums
#
# print(timeit.timeit(even_numbers_with_comprehension))
# print(timeit.timeit(even_numbers_with_loop))

text = input()
vowels = ["a", "u", "e", "i", "o", "A", "U", "E", "I", "O"]
no_vowels = "".join([x for x in text if x not in vowels])
print(no_vowels)