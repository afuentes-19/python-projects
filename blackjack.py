import sys
import random
import time
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
#define functions
def dealCards():
    hand = []
    hand.append(random.choice(deck))
    hand.append(random.choice(deck))
    return hand 

def extraCard(hand, player):
    newCard = random.choice(deck)
    hand.append(newCard)
    if player == "user":
        print(f"You got a {newCard}")
        print(f"Your cards are: {playerCards}")
    if player == "dealer":
        print(f"The dealer got a {newCard}")
        print(f"The dealer's cards are: {dealerCards}")

def calculateScore(hand):
    score = 0
    for card in hand:
        score += card
    return score

def determineWinner(playerHand, dealerHand):
    playerScore = calculateScore(playerHand)
    dealerScore = calculateScore(dealerHand)
    while dealerScore < 16 and dealerScore <= 21:
        print("The dealer has less than 16, so they will draw another card.")
        extraCard(dealerCards, "dealer")
        dealerScore = calculateScore(dealerHand)
    print(f"You score is {playerScore}")
    print(f"The dealer's score is {dealerScore}")
    if playerScore > dealerScore or dealerScore > 21: 
        print("Congratulations, you win booboo <333 Mwahh!")
    elif playerScore == dealerScore:
        print("Tie game!")
    else:
        print("The dealer had a higher score than you, game over!")

#initial variables
playerCards = []
dealerCards = []
keepHitting = False
gameOver = False
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
art = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   >
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
toPlay = input("Would you like to play a game of Blackjack? Enter 'y' for yes or 'n' for no.\n")
if toPlay.lower() == 'y':
    print(art)
    print("Welcome to Blackjack!")
else:
    print("Goodbye!")
    sys.exit()
print("The dealer deals two cards to you...")
time.sleep(1)
playerCards = dealCards()
print(f"Your two cards are: {playerCards}")
print(f"The dealer deals two cards to himself...") 
time.sleep(1)
dealerCards = dealCards()
print(f"The dealer has 2 cards: [{dealerCards[0]},X]")
if calculateScore(playerCards) == 21:
    print("Congrats you won!")
    sys.exit()
else:
    hitAnswer = input("Would you like another card? Enter 'y' for yes or 'n' for no\n")
    if hitAnswer == 'y':
        keepHitting = True
while keepHitting:
    extraCard(playerCards, "user")
    if calculateScore(playerCards) > 21:
        print("Bust! You lose.")
        sys.exit()
    hitAnswer = input("Would you like another card? Enter 'y' for yes or 'n' for no\n")
    if hitAnswer == 'n':
        keepHitting = False
determineWinner(playerCards, dealerCards)
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.