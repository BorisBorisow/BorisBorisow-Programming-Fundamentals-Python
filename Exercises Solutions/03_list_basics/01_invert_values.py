list_of_numbers = input().split()
opposite_numbers = []

# for current_index in range(len(list_of_numbers)):
# current number= int(list_of_numbers[current_index])

for element in list_of_numbers:
    opposite_numbers.append(-int(element))
    
print(opposite_numbers)