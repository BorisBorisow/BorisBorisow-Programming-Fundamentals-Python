some_string = input()
digits = ""
letters = ""
symbols = ""

for ch in some_string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        symbols += ch

print(digits)
print(letters)
print(symbols)