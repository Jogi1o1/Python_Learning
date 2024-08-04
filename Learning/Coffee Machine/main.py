from data import MENU, resources


def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    dollar = (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)

    return dollar


def check_resources(coffee, water, milk):
    if resources["water"] < water:
        print("Not enough water")
        return resources["water"]
    elif resources["coffee"] < coffee:
        print("Not enough coffee")
        return resources["coffee"]
    elif resources["milk"] < milk :
        print("Not enough milk")
        return resources["milk"]


def coffee_resources(coffee_type):
    if coffee_type == "espresso":
        return {"water": 50, "coffee": 18, "milk": 0}
    elif coffee_type == "latte":
        return {"water": 200, "coffee": 24, "milk": 150}
    elif coffee_type == "cappuccino":
        return {"water": 250, "coffee": 24, "milk": 100}
    else:
        return resources


def coffee(coffee_type):
    change = 0
    if coffee_type == "report":
        print(resources)
    elif coffee_type == "espresso":
        dollars = money()
        change = dollars - MENU["espresso"]["cost"]
        if resources["water"] >= 50 and resources["coffee"] >= 18 and change >= 0:
            print(f"Here is ${change} in change.\nHere is your espresso ☕️. Enjoy!")
            resources["water"] -= 50
            resources["coffee"] -= 18
        elif change < 0:
            print(f"Sorry that's not enough money. Money refunded ${dollars}.")
        else:
            check_resources(resources["coffee"], resources["water"], resources["milk"])
    elif coffee_type == "latte":
        dollars = money()
        change = dollars - MENU["latte"]["cost"]
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150 and change >= 0:
            print(f"Here is ${change} in change.\nHere is your latte ☕️. Enjoy!")
            resources["water"] -= 200
            resources["coffee"] -= 24
            resources["milk"] -= 150
        elif change < 0:
            print(f"Sorry that's not enough money. Money refunded ${dollars}.")
        else:
            check_resources(resources["coffee"], resources["water"], resources["milk"])
    elif coffee_type == "cappuccino":
        dollars = money()
        change = dollars - MENU["cappuccino"]["cost"]
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100 and change >= 0:
            print(f"Here is ${change} in change.\nHere is your cappuccino ☕️. Enjoy!")
            resources["water"] -= 250
            resources["coffee"] -= 24
            resources["milk"] -= 100
        elif change < 0:
            print(f"Sorry that's not enough money. Money refunded ${dollars}.")
        else:
            print(check_resources(resources["coffee"], resources["water"], resources["milk"]))


while resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    coffee(user_choice)
