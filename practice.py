import math

def greet_with(name, location, num):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    print(math.ceil(num))

def my_function():
    result = 3 * 2
    return result

def cap_name(f_name, l_name):
    """Takes a first and last name and formats it 
    to return the title case version of the name."""
    capitalized = f_name.capitalize() + " " + l_name.capitalize() 
    return capitalized

if __name__ == "__main__":
    full_name = input("Please enter your full name with the format - first-name<space>last-name all lower-case\nIf you have more than one last name, put a - between it\n")
    print(f"You gave me {full_name}")
    name = full_name.split(" ")
    firstName = name[0]
    lastName = name[1]
    print(f"First name is {firstName}")
    print(f"Last name is {lastName}")
    capitalized = cap_name(firstName, lastName)
    print(capitalized)

    # my_dictionary = {"Bug": "An error in a program that prevents it from running as expected", "Function": "A piece of code that you can easily call over and over again", "Loop": "The action of doing something over and over again"}
    # print(my_dictionary["Bug"])

    # #adding new items 
    # my_dictionary["Alan"] = "The coolest guy"
    # print(my_dictionary)
    # num = 55 
    # if 70 < num < 80:
    #     print("Grade is C")

    # #nesting 
    # capitals = {
    #     "France": "Paris", 
    #     "Germany": "Berlin",
    # }
    # travel_log = {
    #     "France": ["Paris", "Lille", "Dijon"],
    #     "Spain": ["Seville", "Barcelona", "Madrid"]
    # }

    # #nesting a dictionary in a dictionary
    # travel_log["France"] = {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}
    
    # #nexting a dictionary in a list
    # travel_log = [
    #     {
    #     "country": "France",
    #     "cities_visited": ["Paris", "Lille", "Dijon"],
    #     "total_visits": 12
    #     },
    #     {
    #     "country": "Germany",
    #     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    #     "total_visits": 5
    #     }
    # ]

    # print(travel_log)

    
    