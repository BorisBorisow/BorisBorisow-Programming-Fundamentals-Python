number_lost_fights = int(input())
helmet_prince = float(input())
sword_prince = float(input())
shield_prince = float(input())
armor_prince = float(input())

total_helmets_broken = number_lost_fights // 2
total_swords_broken = number_lost_fights // 3
total_shields_broken = number_lost_fights // 6
total_armors_broken = total_shields_broken // 2 # Всеки 2ри път се намира с // целочислено деление
expenses = ((total_helmets_broken * helmet_prince) + (total_swords_broken * sword_prince) + (total_shields_broken * shield_prince) + (total_armors_broken * armor_prince))
print(f"Gladiator expenses: {expenses:.2f} aureus")

