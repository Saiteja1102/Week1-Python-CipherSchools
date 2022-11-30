# exercise , # Number guessing game

winning_number = 11
guess = int(input("Guess a number:"))
if guess == winning_number:
    print("YOU WON!!!!")
else:
    if guess < winning_number:
        print("too low")
    else:
        print("too high")