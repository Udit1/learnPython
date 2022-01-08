# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

t = (name1 + name2).count("t")
r = (name1 + name2).count("r")
u = (name1 + name2).count("u")
e = (name1 + name2).count("e")

total_true = t + r + u + e

l = (name1 + name2).count("l")
o = (name1 + name2).count("o")
v = (name1 + name2).count("v")
e = (name1 + name2).count("e")
total_love = l + o + v + e

total_score = int(str(total_true) + str(total_love))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
