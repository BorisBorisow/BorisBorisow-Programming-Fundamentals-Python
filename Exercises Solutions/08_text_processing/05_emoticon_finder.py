# def emoticon_finder(text):
#     for el in text:
#         if ":" in el:
#             print(el[:2])
#
#
# text = input().split(" ")
# emoticon_finder(text)

def emoticon_finder(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ":" and text[i + 1] != " "]
    print("\n".join(result))


text = input()
emoticon_finder(text)
