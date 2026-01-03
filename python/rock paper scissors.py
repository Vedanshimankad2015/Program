import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock🗻")
    print("2. Paper📄")
    print("3. Scissors✂️")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def choice_to_word(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def determine_winner(user, computer):
    if user == computer:
        return "It's a Tie 🤝"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "You win 🎉"
    else:
        return "Computer wins 💻"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nYour choice:", choice_to_word(user_choice))
        print("Computer choice:", choice_to_word(computer_choice))

        result = determine_winner(user_choice, computer_choice)
        print("\nResult:", result)

        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing 😊")
            break

if __name__ == "__main__":
    play_game()
