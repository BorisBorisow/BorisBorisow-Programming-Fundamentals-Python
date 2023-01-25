import re

valid_destinations = []
len_destinations = 0
pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"
place = input()

result = re.finditer(pattern, place)

for destination in result:
    valid_destinations.append(destination.group(2))

for distance in valid_destinations:
    len_destinations += len(distance)

to_print = "".join(valid_destinations)
print(f"Destinations: {to_print}")
print(f"Travel Points: {len_destinations}")