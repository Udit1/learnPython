import random
words = ["Hello", "Apple", "Banana", "Cat"]

word = random.choice(words)
print(f"The choosen word is {word}")

display = []
for _ in word:
    display += "_"

print(display)

user_input = input("\nGuess a letter")
for position in range(len(word)):
    if user_input == word[position]:
        display[position] = word[position]
        print(display)
    else:
        print("Wrong")
