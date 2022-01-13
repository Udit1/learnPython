import random
words = ["Hello", "Apple", "Banana", "Cat"]

word = random.choice(words)
print(word)

user_input = input("\nGuess a letter")
for a in word:
    if user_input == a:
        print("Right")
    else:
        print("Wrong")
