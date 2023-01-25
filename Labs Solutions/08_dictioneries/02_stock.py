# inventory = input().split(" ")
# inventory_products = {inventory[i]: int(inventory[i + 1]) for i in range(0, len(inventory), 2)}
#
# product_to_search = input().split(" ")
#
# for product in product_to_search:
#     if product in inventory_products:
#         print(f"Sorry, we dont\'t have {product}")
#     else:
#         print(f"We have {inventory_products[product]} of {product} left")

invetory = input().split(" ")
invetory_products = {invetory[i]: int(invetory[i + 1]) for i in range(0, len(invetory), 2)}
# invetory_products = {}
# for i in range(0, len(invetory), 2):
#     invetory_products[invetory[i]] = int(invetory[i + 1])
# print(invetory_products)
searched_products = input().split(" ")

for product in searched_products:
    if product not in invetory_products:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {invetory_products[product]} of {product} left")
