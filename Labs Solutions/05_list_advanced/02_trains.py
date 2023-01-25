number = int(input())
wagons = [0] * number

while True:
    command = input()
    if command == "End":
        break

    data = command.split()
    current_command = data[0]

    if current_command == "add":
        add_people = int(data[1])
        wagons[-1] += add_people

    elif current_command == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] += number_of_people

    elif current_command == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        wagons[index] -= number_of_people

print(wagons)