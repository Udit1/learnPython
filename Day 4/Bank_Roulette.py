import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# c = random.randint(0, len(names) - 1)
# print(f"{names[c]} is going to buy the meal today!")
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")
