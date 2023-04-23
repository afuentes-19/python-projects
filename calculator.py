import sys
#addition
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1,n2):
    return n1 * n2

#division
def divide(n1, n2):
    return n1/n2

answer = 0
logo = """
____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator(): 
    continueCalculating = True
    print(logo)
    num1 = float(input("What is the first number? "))


    while continueCalculating: 
        print(f"The current number is {num1}")
        num2 = float(input("What is the next number? "))
        print("Here are the operations:")
        for operation in operations.keys():
            print(operation)

        operation = input("Which operation would you like to do? ")
        functionName = operations[operation]

        answer = functionName(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")
        
        userAnswer = input(f"Would you like to continue calculating with {answer}? Enter \n'y' for yes,\n'c' to start a new calculation, or \n'n' to exit \n")
        if userAnswer == 'y':
            continueCalculating = True
            num1 = answer
        elif userAnswer == 'c': 
            continueCalculating = False
            calculator() 
        else:
            sys.exit()

calculator()