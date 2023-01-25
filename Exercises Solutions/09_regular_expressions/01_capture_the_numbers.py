import re

matches_list = []
text = input()
regex = r"\d+"
while text:
    match = re.findall(regex, text)
    if match:
        matches_list.extend(match) # Този екстенд поставя елементите в листа разопаковани, а не като отделен лист
    text = input()

print(*matches_list, sep = " ") # разопаковане на листа от числата, където сепаратора е space
#print(" ".join(matches_list), end= " ")

