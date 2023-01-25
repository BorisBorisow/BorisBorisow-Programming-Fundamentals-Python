import re

string = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

valid_nums = re.finditer(pattern, string)
valid_nums = [num.group() for num in valid_nums]
print(*valid_nums)

# import re
#
# string = input()
#
# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
#
# result = re.finditer(pattern, string)
# for match in result:
#     print(match.group(), end=" ")