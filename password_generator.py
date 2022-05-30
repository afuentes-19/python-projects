#Random password generator

import string
import random 
import sys

lower_characters = list(string.ascii_lowercase)
upper_characters = list(string.ascii_uppercase)
nums = []
password = ""
for i in range(0,10):
    nums.append(i)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '^', '@', '+']
print("Welcome to the MyPassword Generator")
n_chars = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
n_symbols = int(input("How many symbols would you like?\n"))

#enforce constraints 
if (n_chars + n_numbers + n_symbols > 50): 
    print("Password is too long. Please run the program to try again.")
    sys.exit()

for n in range(0,n_chars):
    case = random.choice([lower_characters, upper_characters])
    letter = random.choice(case)
    password+= letter
for n in range(0,n_numbers):
    password += str(random.choice(nums))
for n in range(0,n_symbols):
    password += random.choice(symbols)
print(f"Here is your generated password: {password}")

