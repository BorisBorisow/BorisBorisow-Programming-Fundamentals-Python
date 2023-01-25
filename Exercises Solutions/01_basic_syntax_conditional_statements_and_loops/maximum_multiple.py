divisor = int(input())
boundary = int(input())
max_num = 0

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        max_num = current_number
        break

print(max_num)

# divisor = int(input())
# boundary = int(input())
#
# for current_number in range(boundary, divisor, -1):
#   if current_number % 2 == 0:
#        break
# print(current_number)