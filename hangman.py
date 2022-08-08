import random 
import hangman_words
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

#update display based on a user's guess
def update_display():
    global game_over
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
    displayWord = "" 
    #todo3 - print 'display' and you should see the guessed letters and blanks
    for letter in display:
        displayWord += letter + " "
    print(displayWord)
    if "_" not in display: 
        game_over = True

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
    guess = input("Guess a letter: ")
    guess = guess.lower()
    #todo2 - loop through each position in the chosen word.
    # if the letter has been guessed, reveal it 
    update_display() 
    if not guess in chosen_word:
        lives -= 1
        print("Lost a life!")
        print(stages[lives])
    if lives == 0:
        game_over = True
        print("Ran out of lives! Game over.")

