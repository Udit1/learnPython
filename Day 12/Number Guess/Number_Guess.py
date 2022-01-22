from random import randint
from Support import logo, thinking


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game():
    print(f"{logo}")
    computer_choose = randint(1, 100)
    print("I am Thinking of a number between 1 to 100")
    thinking()

    print(computer_choose)
    TURNS = difficulty()

    user_choice = 0
    while user_choice != computer_choose:
        print(f"You have got {TURNS} to make the Guess")
        user_choice = int(input("Enter any Number between 1 to 100"))
        print(f"You have choosen {user_choice}")
        TURNS = check_answer(computer_choose, user_choice, TURNS)

        if TURNS == 0:
            break
        elif user_choice != computer_choose:
            print("Guess Again!!")


def check_answer(computer_choose, user_choice, TURNS):

    if user_choice < computer_choose:
        print("Too Low")
        TURNS -= 1
        return TURNS
    elif user_choice == computer_choose:
        print("Correct")
    else:
        print("Too High")
        TURNS -= 1
        return TURNS


def difficulty():
    level = int(input("""
    Choose the Difficulty Level:
            1. Easy
            2. Hard
    """))
    if level == 1:
        return 10
    else:
        return 5


game()
