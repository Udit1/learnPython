import random
words = ["hello", "apple", "banana", "cat", "dog", "eagle", "fish"]

word = random.choice(words)
print(f"The choosen word is {word}")

display = []
life = 3
end_of_game = False
for _ in word:
    display += "_"

print(display)

while not end_of_game:
    user_input = input("\nGuess a letter\n")
    for position in range(len(word)):
        if user_input == word[position]:
            display[position] = word[position]
            print(display)

    if "_" not in display:
        end_of_game = True
        print("You Won!")
