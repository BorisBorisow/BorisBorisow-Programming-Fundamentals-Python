import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != number:
    if guess > number:
        print(guess, "was too high. Try again.")
    elif guess < number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")