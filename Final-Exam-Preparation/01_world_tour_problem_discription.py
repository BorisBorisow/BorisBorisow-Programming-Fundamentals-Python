stops = input()
command = input()
while not command == "Travel":
    data = command.split(":")
    command = data[0]

    if command == "Add Stop":
        index = int(data[1])
        value = str(data[2])
        if index in range(len(stops)):
            stops = stops[:index] + value + stops[index:]

    elif command == "Remove Stop":
        start_index = int(data[1])
        stop_index = int(data[2])
        if start_index in range(len(stops)) and stop_index in range(len(stops)):
            stops = stops[:start_index] + stops[stop_index + 1:]


    elif command == "Switch":
        old_stop = data[1]
        new_stop = data[2]
        stops = stops.replace(old_stop, new_stop)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")


# def add_stop(stops_str, idx, str):
#     if idx in range(len(stops_str)):
#         return stops_str[:idx] + str + stops_str[idx:]
#
#     return stops_str
#
#
# def remove_stop(stops_str, start, stop):
#     if start in range(len(stops_str)) and stop in range(len(stops_str)):
#         return stops_str[:start] + stops_str[stop + 1:]
#
#     return stops_str
#
#
# def switch(stops_str, old, new):
#     return stops_str.replace(old, new)
#
#
# stops = input()
#
# while True:
#
#     data = input()
#
#     if data == "Travel":
#         break
#
#     split_data = data.split(':')
#
#     command = split_data[0]
#
#     if command == "Add Stop":
#
#         index = int(split_data[1])
#
#         string = split_data[2]
#
#         stops = add_stop(stops, index, string)
#
#     elif command == "Remove Stop":
#
#         start_index = int(split_data[1])
#
#         stop_index = int(split_data[2])
#
#         stops = remove_stop(stops, start_index, stop_index)
#
#     elif command == "Switch":
#
#         old_string = split_data[1]
#
#         new_string = split_data[2]
#
#         stops = switch(stops, old_string, new_string)
#
#     print(stops)
#
# print(f"Ready for world tour! Planned stops: {stops}")
