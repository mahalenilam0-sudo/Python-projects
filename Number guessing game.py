#AI Number Guessing Game
import random

attempts = 0

while True:
    guess = int(input("Enter guess: \t"))
    attempts += 1
    print("You guessed in", attempts, "attempts")

while True:
 if attempts <= 5:
    print("Very close!")

 elif attempts <= 15:
    print("Close!")

 else:
    print("Far away!")

max_attempts = 5
while True:
 if attempts >= max_attempts:
    print("Game Over!")
    break

while True:
    again = input("Would you like to Play again? (yes/no):\t")
    if again.lower() != "yes":
        print("Thank you! Come again. ;):")




