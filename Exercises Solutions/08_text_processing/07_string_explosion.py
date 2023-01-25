text = input()
strength = 0
new_text = ''
for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        strength += int(text[index+1])
        new_text += text[index]
    else:
        new_text += text[index]
print(new_text)

# text = list(input())
# strength = 0
#
# for i, ch in enumerate(text):
#     if ch == ">":
#         strength += int(text[i + 1])
#     if strength > 0 and ch.isalnum():
#         text[i] = "#"
#         strength -= 1
#
# print("".join(text).replace("#", ""))
