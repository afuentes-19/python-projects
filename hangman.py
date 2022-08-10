import random 
import hangman_words
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
import os

#update display based on a user's guess
def update_display():
    global game_over
    global display
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
    #when the user wins
    if "_" not in display: 
        game_over = True
        print("Congrats you won!")
        print(f"Word to guess: {' '.join(display)}")
        print(stages[lives-1])

#Step 0
print(logo)
print("Welcome to Hangman!")

#Step 1 
guessedLetters = []
correctGuessed = []
game_over = False 
lives = len(stages)

#todo1 - Randomly choose a word from the list and assign it to a variable called chosen word
chosen_word = random.choice(word_list)
chosen_word_str = chosen_word
blank = '_'
display = []
displayWord = ""

#convert chosen word to list
chosen_word = list(chosen_word)

#initial set up to put blanks for each character in the chosen word
for character in range(len(chosen_word)):
    display.append('_')

#continue the game until the word has been guessed
while not game_over:
    print(f"Word to guess: {' '.join(display)}")
    print(stages[lives-1])
    guess = input("Guess a letter: ")
    while guess in guessedLetters:
        guess = input("Already guessed this letter, please guess again: ")
        guess = guess.lower()
    guess = guess.lower()
    guessedLetters.append(guess)
    #todo2 - loop through each position in the chosen word.
    # if the letter has been guessed, reveal it 
    os.system("cls")
    update_display()
    if not guess in chosen_word:
        lives -= 1
        print("Lost a life!")
    if lives == 0:
        game_over = True
        print("Ran out of lives! Game over.")
        print(f"Word to guess was {chosen_word_str}. Thanks for playing!")




