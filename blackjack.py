import sys
import random
import time
############### Blackjack Project #####################
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
## If the dealer has less than 16, they get to draw again 

##################### Hints #####################

###########################################
##  Define functions ##
###########################################
def dealCards(num, player):
    hand = []
    hiddenMode = False
    if player == "user":
        hand = playerCards
    else:
        hand = dealerCards
        if len(hand) < 2:
            hiddenMode = True
    for n in range(num):
        newCardIndex = random.randrange(len(deck))
        newCard = deck[newCardIndex]
        # user drew face card (Jack, King, Queen)
        if newCardIndex >= 10 and player == "user":
            faceCardIndex = newCardIndex % 10
            #print(f"Face card index is {faceCardIndex}")
            newCard = faceCards[faceCardIndex]
            print(f"You got a {newCard}")
            print(f"Your {newCard} has a value of 10, so a 10 has been added to your hand")
            newCard = 10
        elif newCardIndex == 0 and player == "user":
            valueNotPicked = True
            newCard = faceCards[0]
            print("You got an Ace!")
            while valueNotPicked:
                aceValue = int(input("An Ace can either have a value of 1 or 11. Enter the value you would like your ace to have: '1' or '11'\n"))
                if aceValue == 1 or aceValue == 11:
                    print(f"Thanks for selecting a value. Your Ace is now {aceValue}")
                    valueNotPicked = False
                else: 
                    print("Sorry, that's not a valid value for an Ace")
            newCard = aceValue
        # dealer logic if dealer draws an Ace
        elif newCardIndex == 0 and player == "dealer":
            if calculateScore(dealerCards) + newCard > 21:
                newCard = 1
            if not hiddenMode:
                print("The dealer got an ace!")
                print(f"The value of the ace will be {newCard}")
        else:
            if player == "user":
                print(f"You got a {newCard}")
            if player == "dealer" and not hiddenMode:
                print(f"The dealer got a {newCard}")
        hand.append(newCard)
    return hand

def calculateScore(hand):
    score = 0
    for card in hand:
        score += card
    return score

def determineWinner(playerHand, dealerHand):
    print("Time to determine who won!")
    time.sleep(1)
    playerScore = calculateScore(playerHand)
    dealerScore = calculateScore(dealerHand)
    while dealerScore < 16 and dealerScore <= 21:
        print("The dealer has less than 16, so they will draw another card.")
        time.sleep(1)
        dealerHand = dealCards(1, "dealer")
        print(f"The dealer's hand is now: {dealerHand}")
        dealerScore = calculateScore(dealerHand)
    for x in range(3): # three dots
        string = "Calculating results" + "." * x
        print("\033[K", string, end="\r") # clear the line, print string and go back to the start
        time.sleep(0.5)
    print()
    print(f"You score is {playerScore}")
    time.sleep(1)
    print(f"The dealer's score is {dealerScore}")
    time.sleep(1)
    # user wins 
    if playerScore > dealerScore or dealerScore > 21: 
        print("Congratulations, you win!")
        if gameWithLives:
            time.sleep(2)
            addWin()
            time.sleep(3)
        else:
            time.sleep(2)
    # tie game
    elif playerScore == dealerScore:
        print("Tie game!")
        if gameWithLives:
            time.sleep(2)
            printPlayerStats()
            print("3 seconds before next game begins...")
            time.sleep(3)
        else:
            time.sleep(2)
    # dealer wins
    else:
        print("The dealer had a higher score than you. The dealer wins!")
        if gameWithLives:
            time.sleep(2)
            loseLife()
            time.sleep(3)
        else:
            time.sleep(2)

def loseLife():
    global lives
    global wins
    lives -= 1
    print(f"You lose a life!")
    printPlayerStats()
    if lives > 0:
        print("3 seconds before next game begins...")

def addWin():
    global lives
    global wins
    global badge
    wins += 1
    if wins == 3:
        badge = "Pro"
        print(f"Congrats, you get the {badge} player badge!")
        time.sleep(2)
    if wins == 5:
        badge = "Elite"
        print(f"Congrats, you get the {badge} player badge!")
        time.sleep(2)
    if wins == 10:
        badge = "Legendary"
        print(f"Amazing!! Congrats, you get the {badge} player badge!!")
        addLife()
        print("Take a moment to celebrate and strategize for the Hall of Fame, All-Star badge! (20 wins)")
        time.sleep(5)
    if wins == 20:
        badge = "HALL OF FAME ALL-STAR"
        print(f"Are you serious?!? You earned the {badge} badge!!")
        print("Take a pause to celebrate!! You hacked the game!!")
        # play music
        time.sleep(10)
    printPlayerStats()
    print("3 seconds before next game begins...")

def addLife():
    global lives
    lives += 1
    time.sleep(1)
    print("Surprise! You earned an extra life!!")
    time.sleep(1)

def printPlayerStats():
    print("***********************")
    print(f"Lives remaining: {lives}")
    print(f"Wins: {wins}")
    if badge:
        print(f"Earned Badge: {badge}")
    print("***********************")

# def changeAce(player, hand):
#     print("Your total score is over 21, but you have an ace!")
#     userAnswer = input("Would you like to change the value of your ace? Enter 'y' for yes")
#     if userAnswer == 'y':


###########################################
##  Define variables ##
###########################################
playerCards = []
dealerCards = []
faceCards = ["Jack", "Queen", "King", "Ace"]
keepHitting = False
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gameOver = False
lives = 3
firstGame = True
wins = 0
gameWithLives = False
badge = ""
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

###########################################
##  START OF GAME ##
###########################################

toPlay = input("Would you like to play a game of Blackjack? Enter 'y' for yes or 'n' for no.\n")
while toPlay.lower() == 'y':
    # reset game 
    playerCards = []
    dealerCards = []
    keepHitting = False
    gameOver = False
    # start game
    print(art)
    print("Welcome to Blackjack!")
    ## ask the user in their first game, if they would like to play in Lives Mode
    if firstGame == True:
        print("Do you want to play with lives mode? (You get 3 lives).")
        livesModeAnswer = input("Enter 'y' for Lives Mode or press any other key for regular, unlimited mode.\n")
        if livesModeAnswer == 'y':
            print("You are now playing with Lives Mode!")
            print("You get 3 lives. Each time the dealer wins, you lose a life")
            print("Let's see how many times you can win, good luck!") 
            time.sleep(3)
            gameWithLives = True
    firstGame = False
    print("***********************\nGAME BEGINS!\n***********************")
    print("The dealer deals two cards to you...")
    time.sleep(1)
    # deals cards
    playerCards = dealCards(2, "user")
    print(f"Your two cards are: {playerCards}")
    print(f"The dealer deals two cards to himself...") 
    time.sleep(1)
    dealerCards = dealCards(2, "dealer")
    print(f"The dealer has two cards: [{dealerCards[0]},X]")
    # determine if user automatically wins
    if calculateScore(playerCards) == 21:
        print("Congrats you got 21 and won!")
        time.sleep(2)
        gameOver = True
        # lives mode: add win 
        if gameWithLives:
            addWin()
            time.sleep(3)
    # ask if the user would like another card 
    else:
        hitAnswer = input("Would you like another card? Enter 'y' for yes or 'n' for no\n")
        if hitAnswer == 'y':
            keepHitting = True
    # keep asking as long as they want another card and they game is not over
    while keepHitting and not gameOver:
        playerCards = dealCards(1, "user")
        print(f"Here are your cards: {playerCards}")
        time.sleep(1)
        playerScore = calculateScore(playerCards)
        print(f"Your score is {playerScore}")
        if playerScore > 21:
            # need extra logic if the player has an ace
            print("Bust! Your score is over 21. You lose.")
            gameOver = True
            time.sleep(2)
            # lose a life if Lives Mode is ON
            if gameWithLives:
                loseLife()
                time.sleep(3)
        if playerScore == 21:
            print("Congrats, you got 21! You win!")
            gameOver = True
            time.sleep(2)
            # add a win and life if Lives Mode is ON
            if gameWithLives:
                addLife()
                addWin()
                time.sleep(3)
        if not gameOver:
            # ask the user if they would like to change the value of their ace if they have one

            # ask the user if they would like anothe card
            hitAnswer = input("Would you like another card? Enter 'y' for yes or 'n' for no\n")
            if hitAnswer == 'n':
                keepHitting = False
    # determine winner
    if not gameOver:
        determineWinner(playerCards, dealerCards)
    # logic for lives mode 
    if gameWithLives and lives > 0:
        toPlay = 'y'
    elif gameWithLives and lives == 0:
        print("Uh oh! You ran out lives.")
        print(f"Your total wins: {wins}")
        if badge:
            print(f"Congrats! Your earned badge is {badge}")
        print("Thanks for playing, goodbye!")
        sys.exit()
    # ask if the users would like to keep playing
    else:
        toPlay = input("Would you like to play another game of Blackjack? Enter 'y' for yes or 'n' for no.\n")
print("Thanks for playing, see you again next time!")
