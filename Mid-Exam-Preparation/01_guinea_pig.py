food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
puppy_weight = float(input()) * 1000
days = 30


for x in range(1, days + 1):

    food -= 300

    if x % 2 == 0:
        hay -= (food * 5) / 100

    if x % 3 == 0:
        cover -= round(puppy_weight / 3)

if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")