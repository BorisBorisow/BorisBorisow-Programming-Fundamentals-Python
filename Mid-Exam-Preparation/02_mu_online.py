data = input().split("|")
health = 100
coins = 0
rooms = 0
condition = False

for room in data:
    command, amount = room.split(" ")
    amount = int(amount)
    rooms += 1
    if command == "potion":
        if health + amount <= 100:
            health += amount
            print(f"You healed for {amount} hp.")
            print(f"Current health: {health} hp.")
        else:
            health_amount = 100 - health
            health = 100
            print(f"You healed for {health_amount} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        coins += amount
        print(f'You found {amount} bitcoins.')
    elif command != "potion" and command != "chest":
        monster = command
        if health - amount <= 0:
            health = 0
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {rooms}")
            condition = True
            break
        else:
            health -= amount
            print(f"You slayed {monster}.")

if not condition:
    print("You've made it!")
    print('Bitcoins:', coins)
    print('Health:', health)
