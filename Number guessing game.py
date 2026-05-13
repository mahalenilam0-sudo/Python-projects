import random

print("\n")
print("==" * 33," 🎮Welcome to Number Guessing Game!🎮 ","==" * 34)

total_score = 0

while True:
    #Difficulty Level Selection
    level = input("\nChoose Difficulty Level (easy/medium/hard): \t").lower()

    if level == "easy":
       num = random.randint(1,50)
       max_attempt = 5
       multiplier = 1
       print("🚀Good start! \nYou have to guess number between  1 to 50. \nYou have total 5 attempts. 👉(Reminder: points will get cut if hint is used!")

    elif level == "medium":
       num = random.randint(1,100)
       max_attempt = 7
       multiplier = 2
       print("🎯 Bravo! You are leveling up!. \nYou have to guess number between  1 to 100. \nYou have total 7 attempts.👉(Reminder: points will get cut if hint is used!")

    elif level == "hard":
       num = random.randint(1,500)
       max_attempt = 10
       multiplier = 3
       print("🔥Excellent! You gonna win the game!. \nYou have to guess number between  1 to 500. \nYou have total 10 attempts.👉(Reminder: points will get cut if hint is used!")

    else:
        print("⚠️Invalid difficulty!")
        continue


    attempts = 0
    hint_used = False
    print("\nThe computer has chosen the the number,can you guess it?")

    #Guess Loop
    while attempts < max_attempt:
        action = input("\nEnter your guess or type 'hint' for a hint :").lower()

        if action == "hint":
            if hint_used:
                print("😢Sorry, you're out of hint!")
                continue
            else:
                hint_range = num // 10
                print(f"🔍Hint: The number is between {max(1,num - hint_range)} and {num + hint_range}")
                hint_used = True
                attempts += 1
                continue
        try:
            guess = int(action)
        except ValueError:
            print("\n⚠️Please enter numbers only or type 'hint' for clue :")
            continue



        attempts += 1

        if guess < num:
            print("Too Low!⬇️")
            print("⚠️Remaining attempts:",max_attempt - attempts)

        elif guess > num:
            print("Too High!⬆️")
            print("⚠️Remaining attempts:", max_attempt - attempts)

        else:
            score = (max_attempt - attempts + 1) * 10 * multiplier
            if hint_used:
                score = int(score * 0.75)
                print("\nCorrect! You won! (Hint penalty applied)🔥👏🏆")
                print(f"\nAttempts used: {attempts}")
                print(f"\n⭐Score: {score}")
                total_score += score
                break
            else:
                print("\nCorrect! You won!🔥👏🏆")
                print(f"\nAttempts used: {attempts}")
                print(f"\n⭐Score: {score}")
                total_score += score
                break
    else:
        print("\nOh No! 💀Game Over!💀")
        print("\nCorrect number was:", num)


    again = input("\n🤔Would you like to Play again? (yes/no):\t").lower()
    if again != "yes":
        print(f"\n📊Final Score : {total_score}")
        print("\n😊Thank you! Come again. ;)")
        break




