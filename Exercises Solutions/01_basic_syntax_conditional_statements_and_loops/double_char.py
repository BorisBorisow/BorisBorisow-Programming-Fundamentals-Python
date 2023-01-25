while True:
    command = input()
    if command == "End":
        break
    if command != "SoftUni":
        for ch in command:
            print(ch * 2, end="")
        print()