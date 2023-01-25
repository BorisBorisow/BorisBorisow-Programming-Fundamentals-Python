import re

phones = input()

regex = "(\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4})\\b"

result = re.findall(regex, phones)

print(", ".join(result))

# import re
#
# phones = input()
#
# regex = r"\+359([\s-])2\1\d{3}\1\d{4}\\b"
# # regex = r"\+359(?P<sep>[\s-])2(?P=sep)\d{3}(?P=sep)\d{4}\\b
#
# matches = re.finditer(regex, phones)
# valid_phones = [match.group() for match in matches]
# print(" ".join(valid_phones))