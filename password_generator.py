#Random password generator

import string
import random 

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
for n in range(0,n_chars):
    case = random.choice([lower_characters, upper_characters])
    letter = random.choice(case)
    password+= letter
for n in range(0,n_numbers):
    password += str(random.choice(nums))
for n in range(0,n_symbols):
    password += random.choice(symbols)
print(f"Here is your generated password: {password}")

