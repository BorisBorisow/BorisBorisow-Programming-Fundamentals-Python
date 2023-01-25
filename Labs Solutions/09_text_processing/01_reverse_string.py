def reversed_string(a_string):
    return a_string[::-1]


while True:
    some_string = input()
    if some_string == "end":
        break
    print(f"{some_string} = {reversed_string(some_string)}")
