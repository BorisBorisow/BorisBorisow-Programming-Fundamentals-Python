def plunder_func(cities_dict, city, killed, stolen):
    cities_dict[city]["popularity"] -= killed
    cities_dict[city]["gold"] -= stolen
    print(f'{city} plundered! {stolen} gold stolen, {killed} citizens killed.')
    if cities_dict[city]["popularity"] <= 0 or cities_dict[city]["gold"] <= 0:
        print(f'{city} has been wiped off the map!')
        del cities_dict[city]
    return cities_dict

def prosper_func(cities_dict, city, gold):
    if city in cities_dict:
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities_dict[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")
    return cities_dict



line = input()
cities = {}

while line != "Sail":
    town, popularity, gold = line.split("||")
    popularity = int(popularity)
    gold = int(gold)

    if town not in cities:
        cities[town] = {"popularity": popularity, "gold": gold}
    else:
        cities[town]["popularity"] += popularity
        cities[town]['gold'] += gold

    line = input()

command = input()

while command != "End":
    data = command.split("=>")

    if data[0] == "Plunder":
        city = data[1]
        killed = int(data[2])
        stolen = int(data[3])
        cities = plunder_func(cities, city, killed, stolen)
    elif data[0] == "Prosper":
        city = data[1]
        gold = int(data[2])
        cities = prosper_func(cities, city, gold)

    command = input()

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

for key, value in cities.items():
    print(f"{key} -> Population: {value['popularity']} citizens, Gold: {value['gold']} kg")





# cities = {}
#
# command = input()
#
# while command != "Sail":
#     tokens = command.split("||")
#     town = tokens[0]
#     people = int(tokens[1])
#     gold = int(tokens[2])
#
#     if town not in cities.keys():  # town not in cities (същото е)
#         cities[town] = [people, gold]
#     else:
#         cities[town][0] += people
#         cities[town][1] += gold
#     command = input()
#
# command = input()
# while command != "End":
#     tokens = command.split("=>")
#     cmd = tokens[0]
#
#     if cmd == "Plunder":
#         town = tokens[1]
#         people = int(tokens[2])
#         gold = int(tokens[3])
#
#         # if cities[town][0] - people > 0 and cities[town][1] - gold > 0:
#         #     cities[town][0] -= people
#         #     cities[town][1] -= gold
#         #
#         # elif cities[town][0] - people < 0 or cities[town][1] - gold < 0:
#         #     if cities[town][0] - people < 0:
#         #         people = cities[town][0]
#         #         cities[town][0] = 0
#         #
#         #     if cities[town][1] - gold < 0:
#         #         gold = cities[town][1]
#         #         cities[town][1] = 0
#         #
#         #     cities.pop(town)
#         #     print(f'{town} has been wiped off the map!')
#
#         cities[town][0] -= people
#         cities[town][1] -= gold
#         print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
#
#         if cities[town][0] <= 0 or cities[town][1] <= 0:
#             cities.pop(town)
#             print(f'{town} has been wiped off the map!')
#
#     elif cmd == "Prosper":
#         town = tokens[1]
#         gold = int(tokens[2])
#
#         if gold < 0:
#             print(f'Gold added cannot be a negative number!')
#         else:
#             cities[town][1] += gold
#             print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
#     command = input()
#
# if len(cities) > 0:  # if cities (същото е)
#
#     print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
#
#     # for key, value in sorted(cities.items(), key=lambda x: (x[1], x), reverse=True):
#     # не достъпваш правилните елементи и мисля, че reverse=True се прилага и върху двете
#     # на теб ти трябва само едното да е descending order
#     for key, value in sorted(cities.items(), key=lambda x: (-x[1][1], x[0])):
#         print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
#
# else:
#     print(f'Ahoy, Captain! All targets have been plundered and destroyed!')