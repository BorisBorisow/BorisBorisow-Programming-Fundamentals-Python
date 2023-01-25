number = int(input())
word = input()
strings = []
second_string = []

for _ in range(number):
    current_word = input()
    strings.append(current_word)
    if word in current_word:
        second_string += [current_word]
print(strings)
print(second_string)

# for i in range(len(strings) - 1, -1, -1):
#     element = strings[i]
#     if word not in element:
#         strings.remove(element)
# print(strings)