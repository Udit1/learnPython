import random
from turtle import clear
from modules import words, arts
from replit import clear

end_of_game = False
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
lives = 6
print(f"{arts.logo}")
print(f'Pssst, the solution is {chosen_word}.', )
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(lives)
        print(f"{arts.stages.pop()}")
        if lives == -1:
            end_of_game = True
            print("You Loss!")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
