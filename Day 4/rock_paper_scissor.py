import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

list_1 = [rock, paper, scissors]

user_choose = int(
    input(
        """
Type 0 for Rock
Type 1 for Paper
Type 2 for Scissors 
"""
    )
)

computer_choose = random.randint(0, 2)

print("User Choose:\t", list_1[user_choose])
print("Compute Choose:\t", list_1[computer_choose])

if (
    (user_choose == 0 and computer_choose == 2)
    or (user_choose == 1 and computer_choose == 0)
    or (user_choose == 2 and computer_choose == 1)
):
    print("You Win!")
elif (
    (user_choose == 0 and computer_choose == 1)
    or (user_choose == 1 and computer_choose == 2)
    or (user_choose == 2 and computer_choose == 0)
):
    print("You Lose!")
elif user_choose == computer_choose:
    print("Tie")
else:
    print("Invalid Choice")
# if user_choose == 0 and computer_choose == 2:
#     print("You Win!")
# elif computer_choose > user_choose:
#     print("You lose!")
# elif computer_choose == user_choose:
#     print("It's a Tie")
# else:
#     print("Invalid Number")
