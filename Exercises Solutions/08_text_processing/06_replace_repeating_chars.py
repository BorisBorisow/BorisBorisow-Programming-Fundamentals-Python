text = input()
current_letter = ""
filtered_letters = []
for letter in text:
    if letter != current_letter:
        current_letter = letter
        filtered_letters.append(letter)
print("".join(filtered_letters))
