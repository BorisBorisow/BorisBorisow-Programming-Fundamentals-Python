# import re
#
# valid_urls = []
# pattern = r"((w{3})\.[A-Za-z0-9\-]+([A-Za-z0-9])(\.[a-z]+)+)"
# sentence = input()
#
# while sentence:
#     matches = re.search(pattern, sentence)
#     if matches:
#         valid_urls.append(matches.group())
#     sentence = input()
# for valid_url in valid_urls:
#     print(valid_url)

import re

pattern = r"(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))"
sentence = input()

while sentence:
    for el in re.finditer(pattern, sentence):
        print(el.group())
    sentence = input()
