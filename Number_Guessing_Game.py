# """Number Gussing Game
# """create a number gussing game where the user has to guss a number between 1 to 50. the user has 10 attempts to guss the
# correct number. after each guss, the program should tell the user if the guss is too high,too low or correct.
import random 
print("Welcome! to the nnumber gussing game.")
number_to_guss = random.randint(1,50)
attempts = 10
secret_number = 24

while attempts > 0:
    guss = input("Guss a number between 1 to 50 or press 'q' to quit:")
    if guss == 'q':
        print("Thanks for playing! Gooodbye.")
        break
    guss = int(guss)
    attempts -=1
    if guss< secret_number:
        print("you gassed to low number")
    elif guss> secret_number:
        print("You guss too high number")
    elif guss == secret_number:
        print("Congratulations! You guss the correct number.")
    else:
        print("sorry, try again.")
        print(f" You have {attempts} attempts left.")
    if attempts ==0:
        print("GAME OVER! You've used all your attempts.")        
