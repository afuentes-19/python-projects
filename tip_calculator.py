print("Welcome to the tip calculator")
bill = float(input("How much was the total bill?"))
percent_tip = float(input("What percentage tip would you like to give?"))
num_people = int(input("How many people would you like to split the bill with? Enter 1 if it's just you."))
percent_tip_add = 1 + (percent_tip/100)
tip_amt = (bill/num_people) * percent_tip_add
tip_amt_rounded = round(tip_amt, 2)
print(f"Each person should pay: ${tip_amt_rounded}")
