import math

def greet_with(name, location, num):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    print(math.ceil(num))

if __name__ == "__main__":
    my_dictionary = {"Bug": "An error in a program that prevents it from running as expected", "Function": "A piece of code that you can easily call over and over again", "Loop": "The action of doing something over and over again"}
    print(my_dictionary["Bug"])

    #adding new items 
    my_dictionary["Alan"] = "The coolest guy"
    print(my_dictionary)
    num = 55 
    if 70 < num < 80:
        print("Grade is C")

    #nesting 
    capitals = {
        "France": "Paris", 
        "Germany": "Berlin",
    }
    travel_log = {
        "France": ["Paris", "Lille", "Dijon"],
        "Spain": ["Seville", "Barcelona", "Madrid"]
    }

    #nesting a dictionary in a dictionary
    travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
    
    #nexting a dictionary in a list
    travel_log = [
        {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
        },
        {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
        }
    ]

    print(travel_log)

    
    #user_name = input("What is your name?")
    #user_location = input("What is your location?")
    #greet_with(location = user_location, name = user_name, num = 7.2) 