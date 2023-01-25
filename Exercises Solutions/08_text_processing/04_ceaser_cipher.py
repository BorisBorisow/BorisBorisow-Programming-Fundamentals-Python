# data = input()
#
# word = ""
# for x in data:
#     word += chr(ord(x) + 3)
# print(word)

def ceasar_cipher(text):
    result = [chr(ord(ch) + 3) for ch in text]
    print("".join(result))

text = input()
ceasar_cipher(text)
