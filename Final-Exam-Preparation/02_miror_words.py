import re

text = input()
pattern = r"([@|#])([A-Za-z]+{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, text)
