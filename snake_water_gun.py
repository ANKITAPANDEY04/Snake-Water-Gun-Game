import random

def snake_gun_water():
    print("Let's play Snake, Water, Gun")
    print("Rules: Snake vs Water -> Snake wins , Water vs Gun -> Water wins , Gun vs Snake -> Gun wins")  

    choices = ["snake", "gun", "water"]
    user_score = 0
    computer_score = 0

    rounds = int(input("Enter the number of rounds you want to play: "))

    for i in range(rounds):
        print(f"\nRound {i+1}")
        user_choice = input("Enter your choice (snake/gun/water): ")
        if user_choice not in choices:
            print("Invalid Choice, try again")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "snake" and computer_choice == "water") or \
             (user_choice == "water" and computer_choice == "gun") or \
             (user_choice == "gun" and computer_choice == "snake"):
            print("You won this round!")
            user_score += 1
        else:
            print("Computer won this round!")
            computer_score += 1

        # Show score after each round
        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

    # Final result after all rounds
    print("\nGame Over!")
    print(f"Final Score -> You: {user_score}, Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You Won the Game!")
    elif user_score < computer_score:
        print("Computer Won! Better luck next time.")
    else:
        print("It's a tie overall!")

snake_gun_water()
