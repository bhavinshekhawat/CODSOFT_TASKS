import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("\n===== FINAL SCORE =====")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thank you for playing!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        continue

    user_choice = choices[int(choice) - 1]
    computer_choice = random.choice(choices)

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: Computer wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
