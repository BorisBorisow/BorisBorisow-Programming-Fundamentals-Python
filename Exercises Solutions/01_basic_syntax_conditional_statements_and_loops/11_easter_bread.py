budget = float(input())
price_of_flour = float(input())
price_of_packet_eggs = price_of_flour * 0.75
needed_milk_for_bread = (price_of_flour * 1.25) / 4

price_of_easter_bread = price_of_packet_eggs + price_of_flour + needed_milk_for_bread
bread_count = 0
count_colored_eggs = 0

while budget >= price_of_easter_bread:
    budget -= price_of_easter_bread
    bread_count += 1
    count_colored_eggs += 3
    if bread_count % 3 == 0:
        bread_count -= bread_count - 2
print(f"You made {bread_count} loaves of Easter bread! Now you have {count_colored_eggs} eggs and {budget:.2f}BGN left.")