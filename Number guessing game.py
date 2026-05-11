import random

print("-- Welcome to Number Guessing Game!-- ")

while True:
    #Difficulty Level Selection
    level = input("\nChoose Difficulty Level (easy/medium/hard): \t").lower()

    if level == "easy":
       num = random.randint(1,50)
       max_attempt = 5

    elif level == "medium":
       num = random.randint(1,100)
       max_attempt = 7

    elif level == "hard":
       num = random.randint(1,500)
       max_attempt = 10

    else:
        print("Invalid difficulty!")
        continue


    attempts = 0

    #Guess Loop
    while attempts < max_attempt:
        try:
            guess = int(input("Enter Your Guess: "))
        except ValueError:
            print("Please enter numbers only!")
            continue


        attempts += 1

        if guess < num:
            print("Too Low!")

        elif guess > num:
            print("Too High!")

        else:
            print("Correct! You won!")
            print("Attempts used:",attempts)
            break
    else:
        print("Oh No! Game Over!")
        print("Correct number was:", num)


    again = input("Would you like to Play again? (yes/no):\t").lower()
    if again != "yes":
        print("Thank you! Come again. ;)")
        break




