#1vi nachin
# data = input().split(" ")
# product_dict = {}
#
# for i in range(0, len(data), 2):
#     product_dict[data[i]] = int(data[i + 1])
# print(product_dict)

# tasks_list = input().split(" ")
# bakery = {}
#
# for el in range(0, len(tasks_list), 2):
#     key = tasks_list[el]
#     value = tasks_list[el +1]
#     bakery[key] = int(value)
# print(bakery)

data = input().split(" ")
bakery = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
print(bakery)

