import random

choice = int(input("Choose 1 for Head and 0 for Tail"))

random_choice = random.randint(0, 1)
print(choice, random_choice)

if choice == random_choice:
    print("You Win!")
else:
    print("Sorry you loss")
