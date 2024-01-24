import random
drinks = ["beer", "wine", "whiskey", "campari", "tequila", "rum", "gin tonic", "rakija"]
try:
    age = int(input("How old are you? "))
    country = input("What country do you live in? ")
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    # Do some sanity checks on age
    if age < 0 or age > 130:
        print("I am sorry, but your age cannot be negative, or greater than 130")

    if age < 18:
        print("I am sorry, but you are too young to play this game anywhere")
    elif age < 21 and country == "US":
        print("I am sorry, but you are too young to play this drinking game in the US. You can play anywhere else")
    elif
        drink = random.choice(drinks)
        print("Drink some", "drink", "thank you for playing, you are", age, "years old")

