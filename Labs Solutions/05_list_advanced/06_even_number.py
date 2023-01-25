numbers = list(map(int, input().split(", ")))
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(indices)

# number_list = list(map(int, input().split(", ")))
# found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else \
#     "no", range(len(number_list)))
# even_indices = list(filter(lambda a: a != "no", found_indices_or_no))
# print(even_indices)