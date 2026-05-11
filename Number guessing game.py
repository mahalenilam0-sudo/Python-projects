#AI Number Guessing Game
import random

print("-- Welcome to Number Guessing Game!-- ")


while True:

     #Difficulty Level Selection
     level = input("\nChoose Difficulty Level (easy/medium/hard): \t").lower()

     if level == "easy":
         secret = random.randint(1,50)

     elif level == "medium":
         secret = random.randint(1,100)

     elif level == "hard":
         secret = random.randint(1,500)

     else:
         print("Invalid difficulty!")
         continue


attempts = 0
max_attempts = 5

#Guess Loop
while True:
    try:
        guess = int(input("Enter Your Guess: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    attempts += 1

    if guess < secret:
        print("Too Low!")

    elif guess > secret:
        print("Too High!")

    else:
        print("Correct! You won!")
        print("Attempts used:",attempts)
        break

else:
   print("Oh No! Game Over!")
   print("Correct number was:", secret)

while True:
    again = input("Would you like to Play again? (yes/no):\t").lower()
    if again != "yes":
        print("Thank you! Come again. ;)")
        break




