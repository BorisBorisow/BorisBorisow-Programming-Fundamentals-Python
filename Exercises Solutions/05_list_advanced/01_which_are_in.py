# first_list = input().split(", ")
# second_list = input().split(", ")
# substrings = []
# for first_word in first_list:
#     for second_word in second_list:
#         if first_word in second_word and first_word not in substrings:
#             substrings.append
#             break
# print(substrings)

first_list = input().split(", ")
second_list = input().split(", ")
substrings = [first_word for first_word in first_list\
              if any(first_word in second_word for second_word in second_list)]
print(substrings)

