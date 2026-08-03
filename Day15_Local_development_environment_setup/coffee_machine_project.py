
menu = {
    "espresso": {
        "ingredients":{
            "water":50,
            "milk":0,
            "coffee":10,
        },
        "cost":1.5,
    },
    "latte": {
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino": {
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "penny" : 0.01,
    "nickel" : 0.05,
    "dime" : 0.10,
    "quarter" : 0.25,    
}

def generate_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

def check_resource_sufficient(choice):
    for item in [key for key in resources.keys() if key != "money"]:
        if resources[item] < menu[choice]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(choice):
    for item, amount in menu[choice]["ingredients"].items():
        resources[item] -= amount


def check_money_sufficient(choice,quaters,dimes,nickles,pennies):
    user_paid = quaters*coins["quarter"] + nickles*coins["nickel"] + dimes*coins["dime"] + pennies*coins["penny"]
    if user_paid < menu[choice]["cost"]:
        print(f"Sorry that's not enough money, Money refunded.")
        return False, 0.0

    resources["money"] += menu[choice]["cost"]
    if user_paid == menu[choice]["cost"]:
        return True, 0.0

    refunded_amount = round(user_paid - menu[choice]["cost"], 2)
    return True, refunded_amount


def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice in ["espresso","latte","cappuccino"]:
            have_sufficient_resources = check_resource_sufficient(choice)
            if have_sufficient_resources:            
                print("Please insert coins.")
                try:
                    quaters = int(input("How many quaters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickles = int(input("How many nickles? "))
                    pennies = int(input("How many pennies? "))
                except ValueError:
                    print("Invalid value")
                    continue
                have_money_sufficient, refunded_amount = check_money_sufficient(choice,quaters,dimes,nickles,pennies)

                if have_money_sufficient:
                    make_coffee(choice)
                    print(f"Here is ${refunded_amount} in change.")
                    print(f"Here is your {choice}. Enjoy!")
            else:
                continue
        elif choice == "report":
            generate_report()
        elif choice == "off":
            exit()
        else:
            print("Wrong input.")
            continue


if __name__ == "__main__":
    main()




