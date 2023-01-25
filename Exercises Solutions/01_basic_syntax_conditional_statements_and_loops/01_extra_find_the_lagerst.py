number = input()
largest_number = sorted(number, reverse=True)

for d, digit in enumerate(largest_number):
    print(digit, end="")