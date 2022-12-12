import os 
import random 
from lists import auctionItems 

def addBidder(name, bidAmt):
    bidders[name] = bidAmt

def determineWinner(bidders):
    highestBid = 0
    result = ""
    for name in bidders:
        print(f"Currently looking at {name} with the bid: {bidders[name]}\n")
        currentBidAmt = bidders[name]
        if currentBidAmt > highestBid:
            highestBid = currentBidAmt
            result = f"The winning bid is by {name} who wins today's item, {todaysItem}, for ${currentBidAmt}. Congratulations!\n"
        elif bidders[name] == highestBid:
            result = "There is a tie!"
    return result 

bidders = {}
moreBidders = True
todaysItem = random.choice(auctionItems)
print("Hello! Welcome to the Auction Game!")

while moreBidders: 
    print(f"Today's bid is for this item: {todaysItem}")
    bidderName = input("What is your name?\n")
    bidderAmt = float(input(f"Welcome to the auction, {bidderName}! How much would you like to bid? (Enter number amount only)\n"))
    nextBidder = input("Is there another bidder? Please enter 'yes' or 'no'.\n")
    addBidder(bidderName, bidderAmt)
    if nextBidder == 'no':
        moreBidders = False
    os.system('cls')

print(determineWinner(bidders))



