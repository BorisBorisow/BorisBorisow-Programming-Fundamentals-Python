data = input().split(".")
data_split = data[0].split("\\")

print(f"File name: {data_split[-1]}")
print(f"File extension: {data[1]}")


# def split_func(name, language):
#     print(f"File name: {name}")
#     print(f"File extension: {language}")
#
# data = input().split(".")
# data_split = data[0].split("\\")
# split_func(data_split[-1], data[1])

