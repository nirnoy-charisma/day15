from data import resources
from data import MENU


def coins():
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.01
    nickles = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def check_enough_resources(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True



def transaction(received_money, cost_drink):
    if received_money >= cost_drink:
        change = round(received_money - cost_drink, 2)
        print(f"here is you change ${change}.")
        return True
    else:
        print("that is not enough. money is refunded")
        return False


def coffee(name, ingredient_drink):
    for item in ingredient_drink:
        resources[item] -= ingredient_drink[item]
    print(f"Here is your {name} ☕️. Enjoy!")

is_on=True
while  is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif choice == "off":
        is_on = False
    else:
        drink = MENU[choice]
        if check_enough_resources(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                coffee(choice, drink["ingredients"])
