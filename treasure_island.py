import random
import time
import sys

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
time_mode = False
game_over = False
hard_mode = False 
time_to_win = 60; 
time_left = 60; 
start_time = 0; 
user_health = 10
user_turns = 10 

# Intro 
print("Welcome to Treasure Island! You are in a beautiful island and ALAS! You see on the brochure that there is TREASURE somewhere on this island!\n" +
    "You're on a journey to find the treasure but you will have to use your wits to survive on this dangerously fun journey!")
hard_mode = input("Enter 'H' for hard mode or enter to continue with normal mode\n")
time_mode_response = input("Want to spice things up with timed mode? Enter 'Y' for Yes or just press enter to continue without timed mode\n")
if time_mode_response == 'Y':
    time_mode = True
    start_time = time.time()
    if hard_mode == 'H':
        hard_mode = True
        time_left = 45
        time_to_win = 45
        print("Timer started, you have 45 seconds to find the treasure!")
    else:  
        print("Timer started, you have 1 minute to find the treasure!")
direction_options = ["left", "right", "forward", "diagonal", "moonwalk"]
wrong_direction = random.choice(direction_options)

# First challenge: the right turn 
user_direction = input("Which direction will you go? Enter one: left, right, forward, diagonal, moonwalk\n")
user_direction = user_direction.lower()
if (user_direction != wrong_direction and user_direction in direction_options): 
    if (user_direction != "moonwalk"):
        print(f"Good choice going {user_direction}!")
    else:
        print(f"Nice move with the {user_direction}! You're doing great.")
    if time_mode:
        time_left = time_to_win - (time.time() - start_time)
        print(f"Time left: {time_left} seconds")
else: 
    print("Oops wrong move! game over.")
    sys.exit() 
    

if (time_mode and time_left < 0):
    print("You ran out of time, slowboat! game over.")
    sys.exit()

# Second Challenge: Fight monsters
if (hard_mode): 
    randomNumMonsters = random.randint(22, 30)
else: 
    randomNumMonsters = random.randint(12, 20)

print(f"   Now, GET READY TO FIGHT! There are {randomNumMonsters} island MONSTERS ready to fight you.\n" +
        "   Each turn you can choose to 'attack', 'heal', or 'run'.\n" +
        "   Entering 'attack' will defeat at least 1 to at most 6 monsters depending on your health. You lose 2 health each time you attack.\n" +
        "   Entering 'heal' will heal yourself with 3 lives and if you have less than 5 lives left or you will get or 1-2 health if you have 5 lives or more. \n (Healing takes 3 seconds if you are in timed mode!)\n" +
        "   Entering 'run' will mean you will rather flight than fight and have to rely on your health, speed, and luck to escape whatever monsters remain!\n" +
        "   Also, you only have 10 TURNS before it gets too dark on the island and you tire of dehydration. So choose wisely.")

turns = 10
heal_count = 0
while randomNumMonsters > 0:
    # game over checks
    if time_mode:
        time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
        if time_left<=0:
            print("You ran out of time! Game over")
            sys.exit()
    if turns < 1:
        print("You ran out of turns!") 
        sys.exit() 

    #user prompt 
    user_action = input("Will you 'attack', 'heal', or 'run'? Enter your selection\n")

    # makes sure user action is interpreted correctly in the case they inputted uppercase characters
    user_action.lower()

    # deduct a turn per selection
    turns -= 1

    # attack
    if user_action == "attack":
        if user_health >= 8:
            randomAttack = random.randint(4, 6)
            randomNumMonsters -= randomAttack
        elif user_health >= 5 and user_health <= 7:
            randomAttack = random.randint(2, 5) 
            randomNumMonsters -= randomAttack  
        elif user_health == 4:
            randomAttack = random.randint(1,3) 
            randomNumMonsters -= randomAttack  
        else: 
            randomNumMonsters -= 1
        user_health -= 2
        if user_health < 1:
            print("You ran out of lives! Game over.")
            sys.exit()
    # heal 
    elif user_action == "heal":
        if user_health >= 5:
            randomHealth = random.randint(1,2)
            user_health += randomHealth
        else: 
            user_health += 3
        if time_mode:
            heal_count += 1

    # run
    elif user_action == "run": 
        if randomNumMonsters >= 5 and user_health <= 5:
            print("You were too low in health and there were too many monsters!\n They caught up to you and they want you to feed them burgers forever. Game over!")
            sys.exit()
        elif randomNumMonsters >=2 and randomNumMonsters <= 5:
            randomRunLuck = random.randint(1,3) 
            print("speed number " + str(randomRunLuck))
            print("With your chances, you had a 33 percent chance to run away!")
        elif randomNumMonsters == 1 and user_health < 6:
            randomRunLuck = random.randint(1,2) + 1
            print("speed number " + str(randomRunLuck))
            print("With your chances, you had a 50 percent chance to run away!")
        elif randomNumMonsters == 1 and user_health >= 6:
            randomRunLuck = random.randint(1,2) + 1
            print("speed number " + str(randomRunLuck))
            if randomRunLuck != 3:
                randomRunLuck = random.randint(1,2) + 1
                print("speed number " + str(randomRunLuck))
                print("With your chances, you had a 75 percent chance to run away!")
        elif user_health >= 12 and randomNumMonsters <8:
            randomRunLuck = random.randint(1,5)
            print("speed number " + randomRunLuck)
            print("With your chances, you had a 20 percent chance to run away!")
        else: 
            randomRunLuck = random.randint(1,25)
            print("With your chances, you had a 4 percent chance to run away!")
            print(randomRunLuck)
 
        if randomRunLuck == 3:
            print("Nice job, you were able to outrun the monsters!")
            randomNumMonsters = 0; 
        else: 
            print("You were too slow to outrun the monsters. You will now feed them their favorite island tacos until they're happy. Game over")
            sys.exit()
    else:
        print("invalid input. try again!")
    
    # let user know of their health status, time status (if time mode), and monsters left!
    print(f"HEALTH CHECK: You have {user_health} health left")
    print(f"MONSTERS LEFT: You have {randomNumMonsters} monsters left")
    print(f"({turns} turns left)")
    if time_mode: 
        time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
        print(f"TIME LEFT: You have {time_left} seconds left!")

#time check
if time_mode:
    time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
    if time_left <= 0:
        print("You ran out of time! Game over")
        print("Time: " + str(time_left))
        sys.exit()

# Third Challenge 
print("The island is full of treasure, and the Queen of Treasure Island has the key to the treasure if you are able to give the people what they want... BURGERS!\n" + 
    "You will prepare the burgers by answering a series of math and trivia questions for each step!")
randomNum1 = random.randint(1,10)
randomNum2 = random.randint(1,10)
randomQuestion = random.randint(1,4)
math_answer = randomNum1 * randomNum2
if (hard_mode):
    math_answer = (randomNum1 * randomNum2) - (randomNum1 + randomNum2)
triviaTypes = ["science", "history", "geography"]
scienceTrivia = [
    "Enter the name of the essential gas so important that allows us to breathe?",
    "What is the nearest planet to the sun?",
    "How many teeth does an adult human have?",
    "What is the name of the largest star in the solar system?"
]
scienceTriviaAnswers = ["oxygen", "mercury", "32", "sun"]
historyTrivia = [
    "Where did the Olympic Games originate?",
    "Who invented the light bulb?",
    "Who was the first woman to fly solo across the Atlantic?",
    "When did World War II end?"
]
historyTriviaAnswers = ["greece", "thomas edison", "amelia earhart", "1945"]
geographyTrivia = [
    "Which country has the largest population in the world?",
    "What is the name of the longest river in Africa? Enter the full name to answer, e.g. Hudson River",
    "What is the only continent without snakes or reptiles?",
    "The country of Suriname is located in which continent?"
]
geographyTriviaAnswers = ["china", "nile river", "antarctica", "south america"]

print("PART 1: THE PATTY")
if hard_mode:
    user_math_answer = input(f"What is ({randomNum1} x {randomNum2}) - ({randomNum1} + {randomNum2})?\n")
else: 
    user_math_answer = input(f"What is {randomNum1} times {randomNum2}?\n")
user_math_answer = int(user_math_answer)
if user_math_answer != math_answer:
    print("wrong answer! brush up on your math, game over.")
    sys.exit()
else: 
    print("Great job, math whiz!")
    if time_mode: 
        time_left = time_to_win - (time.time() - start_time)
        print(f"TIME CHECK: You have {time_left} seconds left!")
#time check
if time_mode:
    time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
    if time_left <= 0:
        print("You ran out of time! Game over")
        print("Time: " + str(time_left))
        sys.exit()

print("PART 2: THE TOPPINGS! (Lettuce, Tomato, Onions, Mayo")
randomTriviaTopic = random.choice(triviaTypes)
print(f" Now it's time to test your trivia in {randomTriviaTopic}")

#science
if randomTriviaTopic == "science":
    user_trivia_answer = input(scienceTrivia[randomQuestion-1] + "\n")
    user_trivia_answer = user_trivia_answer.lower()
    if user_trivia_answer == scienceTriviaAnswers[randomQuestion-1]:
        print("Great job mad scientist! You put delicious toppings on the burger and it's ready!")
    else: 
        print("oops, wrong answer! game over")
        sys.exit()
if randomTriviaTopic == "history":
    user_trivia_answer = input(historyTrivia[randomQuestion-1] + "\n")
    user_trivia_answer = user_trivia_answer.lower()
    if user_trivia_answer == historyTriviaAnswers[randomQuestion-1]:
        print("Great job time traveller! You put delicious toppings on the burger and it's ready!")
    else: 
        print("oops, wrong answer! game over")
        sys.exit()
if randomTriviaTopic == "geography":
    user_trivia_answer = input(geographyTrivia[randomQuestion-1] + "\n")
    user_trivia_answer = user_trivia_answer.lower()
    if user_trivia_answer == geographyTriviaAnswers[randomQuestion-1]:
        print("You know your maps! Did you use Google Maps? Anyways, you put delicious toppings on the burger and it's ready!")
    else: 
        print("oops, wrong answer! game over")
        sys.exit()

#time check
if time_mode:
    time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
    if time_left<=0:
        print("You ran out of time! Game over")
        print("Time: " + str(time_left))
        sys.exit()
    print(f"TIME CHECK: You have {time_left} seconds left!")

print("PART 3: THE ASSEMBLY!")
if hard_mode:
    answer = "This deliciously salivating burger is for the amicable people of Treasure Island!"
else:
    answer = "This burger is for the people of Treasure Island!"
user_statement = input("Enter the following phrase precisely:\n" + answer + "\n")
if user_statement == answer:
    print("The burgers are ready and are being served to the people of Treasure Island!")
else: 
    print("You dropped the burgers on the ground! Game over")
    sys.exit()

#time check
if time_mode:
    time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
    if time_left<=0:
        print("You ran out of time! Game over")
        print(f"Time: {time_left}")
        sys.exit()
    print(f"TIME CHECK: You have {time_left} seconds left!")


# which hand
randomHand = random.choice(["right", "left"])

# The Queen gives the key to the treasure!
print(f"The Queen of Treasure Island thinks you have done a splendid job and tells you to approach the guard for the treasure.\n" +
    f"One more thing: she says to pick the {randomHand} hand from the Guard when he asks you")
if hard_mode: 
    print(f"The Queen of Treasure Island has also noted to not forget to mind your manners and say please after your response. No commas needed")
    randomHand += " please"

user_which_hand = input("You approach the Guard, and he says he has the key in one of his hands. He is asking which hand do you choose? Enter 'right' or 'left'\n")
user_which_hand.lower()

if user_which_hand == randomHand:
    if time_mode: 
        time_left = time_to_win - (time.time() - start_time) - (heal_count*3)
        if time_left<=0:
            print("You ran out of time! Game over")
            print(f"Time: {time_left}")
            sys.exit() 
        else: 
            print("Congrats! You win the treasure and the game! Thanks for playing!")
            print(f"Time left: {time_left}")
    else: 
        print("Congrats! You win the treasure and the game! Thanks for playing!")
else: 
    print("Ooops! You did not listen to the Queen! Game over") 
    sys.exit() 





