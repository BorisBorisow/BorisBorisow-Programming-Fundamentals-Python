# script = input()
# new_massage = []
# for i in script:
#     new_massage.append(i)
#
# while True:
#     command = input().split("|")
#     if command[0] == "Decode":
#         print(f"The decrypted message is: {''.join(new_massage)}")
#         break
#
#     if command[0] == "Move":
#         item = new_massage[0:int(command[1])]
#         for i in item:
#             new_massage.append(i)
#         del new_massage[0:int(command[1])]
#
#     elif command[0] == "Insert":
#         new_massage.insert(int(command[1]), str(command[2]))
#
#     elif command[0] == "ChangeAll":
#         for i in range(len(new_massage)):
#             if new_massage[i] == command[1]:
#                 new_massage[i] = command[2]
#
#

script = input()
command = input().split("|")

while command[0] != "Decode":
    if command[0] == "Move":
        num = int(command[1])
        script = script[num:] + script[:num]
    elif command[0] == "Insert":
        index = int(command[1])
        value = str(command[2])
        script = script[:index] + value + script[index:]
    elif command[0] == "ChangeAll":
        substring = str(command[1])
        replace = str(command[2])
        script = script.replace(substring, replace)

    command = input().split("|")

print(f"The decrypted message is: {script}")

# 3
def move_func(message, letters):
    message = message[letters:] + message[:letters]
    return message

def insert_func(message, position, letter):
    message = message[:position] + letter + message[position:]
    return message

def change_func(message, old, new):
    message = message.replace(old, new)
    return message



encrypted_message = input()

# while True:
#     command = input()
#     if command == "Decode":
#         break
#
#     data = command.split("|")
#     current_command = data[0]
#
#     if current_command == "Move":
#         letters = int(data[1])
#         encrypted_message = move_func(encrypted_message, letters)
#
#     elif current_command == "Insert":
#         position = int(data[1])
#         letter = data[2]
#         encrypted_message = insert_func(encrypted_message, position, letter)
#
#     elif current_command == "ChangeAll":
#         old_letter = str(data[1])
#         new_letter = str(data[2])
#         encrypted_message = change_func(encrypted_message, old_letter, new_letter)
#
# print(f"The decrypted message is: {encrypted_message}")