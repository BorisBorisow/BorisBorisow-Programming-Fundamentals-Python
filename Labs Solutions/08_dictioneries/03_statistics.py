# text = input()
# store = {}
#
# while text != "statistics":
#
#     text = text.split(": ")
#     product = text[0]
#     quantity = int(text[1])
#
#     if product in store.keys():
#         store[product] += quantity
#     else:
#         store[product] = quantity
#
#     text = input()
#
# count = len(store.keys())
# total = sum(store.values())
# print("Products in stock:")
# for product in store:
#     print(f"- {product}: {store[product]}")
# print(f"Total Products: {count}")
# print(f"Total Quantity: {total}")

store = {}
while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in store:
        store[product] = quantity
    else:
        store[product] += quantity

print("Products in stock:")
products_representation = [f"- {item}: {str(store[item])}" for item in store]
print("\n".join(products_representation))
print(f"Total Products: {len(store)}")
print(f"Total Quantity: {sum(store.values())}")