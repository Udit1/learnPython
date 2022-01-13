import random
words = ["hello", "apple", "banana", "cat", "dog", "eagle", "fish"]

word = random.choice(words)
print(f"The choosen word is {word}")

display = []
life = 3
for _ in word:
    display += "_"

print(display)

while "_" in display:
    user_input = input("\nGuess a letter\n")
    for position in range(len(word)):
        if user_input == word[position]:
            display[position] = word[position]
            print(display)

if "_" not in display:
    print("You Won!")
