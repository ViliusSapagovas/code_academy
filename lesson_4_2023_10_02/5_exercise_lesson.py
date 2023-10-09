from random import randint

random_number = randint(1, 10)
guess_number = int(input("Guess the number from 1 to 10: "))

if guess_number == random_number:
    print(f"You've guessed it! It is {random_number}")
else:
    print(f"Oops, you missed it, it was {random_number}")