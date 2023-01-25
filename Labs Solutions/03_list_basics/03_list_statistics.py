numbers = int(input())

count_of_positives = []
negatives = []

for num in range(numbers):
    current_num = int(input())
    if current_num >= 0:
        count_of_positives += [current_num]
    else:
        negatives += [current_num]

print(count_of_positives)
print(negatives)
print(f"Count of positives: {len(count_of_positives)}")
print(f"Sum of negatives: {sum(negatives)}")
