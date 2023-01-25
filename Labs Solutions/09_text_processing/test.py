def multiline_input(text):
    print(text)
    multiline_input = ""

    while True:
        some_string = input()

        if some_string != "":
            multiline_input += some_string + "\n"
        else:
            break

    return multiline_input

print(multiline_input("Please enter some string: "))