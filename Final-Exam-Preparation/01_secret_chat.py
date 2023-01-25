text = input()

while True:
    command = input().split(":|:")

    if command[0] == "Reveal":
        print(f"You have a new text message: {text}")
        break
    if command[0] == "ChangeAll":
        alt = command[1]
        new = command[2]
        if alt in text:
            text = text.replace(alt, new)
            print(text)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            text += substring[::-1]
            print(text)
        else:
            print("error")

    elif command[0] == "InsertSpace":
        index = int(command[1])
        text = text[:index] + " " + text[index:]
        print(text)
