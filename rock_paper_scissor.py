import random
print("""Welcome to Rock, Paper, Scissors!  

Rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Let's play!
""")
while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
    if user_choice == 'q':
        print("Thanks for playing! Goodbye.")
        break
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
            print("Computer wins!")    


print("Thanks For Playing!")