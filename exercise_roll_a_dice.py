import random

print("Welcome! to the game of rolling a dice.")
while True:
    choice = input("press 'enter' to roll the dice or 'q' to quit:")

    if  choice == 'q':
        print("Thanks for playing! Goodbye.")
        break
    elif choice == '':
        dice_roll = random.randint(1,6)
        print(f"You rolled a {dice_roll}!")

    else:
        print("sorry,invalid input. Please try again.")




print("!!GAME OVER!!")             