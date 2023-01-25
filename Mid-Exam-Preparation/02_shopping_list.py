

items = input().split("!")

while True:
    initial = input()
    if initial == "Go Shopping!":
        print(", ".join(items))
        break

    data = initial.split(" ")
    command = data[0]

    if command == "Urgent":
        item = data[1]
        if item in items:
            continue
        else:
            items.insert(0, item)
    elif command == "Unnecessary":
        item = data[1]
        if item in items:
            items.remove(item)

    elif command == "Correct":
        old_item = data[1]
        new_item = data[2]
        if old_item in items:
            for i in range(len(items)):
                if items[i] == old_item:
                    items[i] = new_item

    elif command == "Rearrange":
        item = data[1]
        if item in items:
            items.remove(item)
            items.append(item)



