version = [int(number) for number in input().split(".")]
version[-1] += 1
for current_index in range(len(version) - 1, -1, -1):
    if version[current_index] > 9:
        version[current_index] = 0
        if current_index - 1 >= 0:
            version[current_index - 1] += 1
print(".".join(str(number) for number in version))

# Втори начин
# version = input()
# version = version.replace(".", "")
# print(int(version)+1)


# Трети начин
# version = input()
# version_num = int(version.replace(".", ""))
# new_version = version_num + 1
# new_version_str = str(new_version)[0] + "." + str(new_version)[1] + "." + str(new_version)[2]
# print(new_version_str)

