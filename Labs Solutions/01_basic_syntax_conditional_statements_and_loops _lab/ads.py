condition = False

for i in range(1, 5):
    for l in range(1, 5):
        if i == 2:
            print(i)
            condition = True
            break
        print(i)

    if condition:
        break
