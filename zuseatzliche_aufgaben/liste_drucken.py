farben = ["Rot", "Orange", "Gelb", "Grün", "Blau"]
print(*farben, sep="\n")
for element in farben:
    print(element.rjust(20), sep="\n")
