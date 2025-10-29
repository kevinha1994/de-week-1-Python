import random

def get_user_choise():
    user_input = input("Enter rock, paper, scissors: ").lower()
    valid_choices = ["rock", "paper", "scissors"]
    while user_input not in valid_choices:
        print("Invalid choice. Try again!")
        user_input = input("Enter rock, paper, scissors: ").lower()
    print(f"You choose {user_input}.")
    return user_input

get_user_choise()
    