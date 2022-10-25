import math

def greet_with(name, location, num):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    print(math.ceil(num))

if __name__ == "__main__":
    user_name = input("What is your name?")
    user_location = input("What is your location?")
    greet_with(location = user_location, name = user_name, num = 7.2) 