print(list(numbers))
numbers = list(numbers)
length = len(numbers)
print(f"Length of the list is: {length}")
i = 4
while i>= 0:
    print(numbers[i])
    i = i-1

#hurdle code
move()
def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
