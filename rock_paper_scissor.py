#Program that plays the rock, paper, scissor game with the computer
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
acceptable_input = [0, 1, 2]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
user_choice = int(user_choice)
while user_choice not in acceptable_input:
    print("Sorry! That's an invalid input. Please try again\n")
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    user_choice = int(user_choice)
computer_choice = random.choice(acceptable_input)

print("Your choice\n")
if (user_choice == 0):
    print(rock + "\n")
elif (user_choice == 1):
    print(paper + "\n")
else:
    print(scissors + "\n")

print("CPU Choice:\n")
if (computer_choice == 0):
    print(rock + "\n")
elif (computer_choice == 1):
    print(paper + "\n")
else:
    print(scissors + "\n")

result= ""
if user_choice == computer_choice:
    result = "tie"
elif user_choice > computer_choice:
    if computer_choice == 0 and user_choice == 2:
        result = "You lose. :("
    else: 
        result = "You win!"
elif computer_choice > user_choice:
    if user_choice == 0 and computer_choice == 2:
        result = "You win!" 
    else:
        result = "You lose. :("
print(result)

    
