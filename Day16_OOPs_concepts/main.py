from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()


def main():
    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice in ["espresso","latte","cappuccino"]:
            item = menu.find_drink(choice)
            have_sufficient_resources = coffe_maker.is_resource_sufficient(item)
            if have_sufficient_resources:            
                # print("Please insert coins.")
                # try:
                #     quaters = int(input("How many quaters?: "))
                #     dimes = int(input("How many dimes?: "))
                #     nickles = int(input("How many nickles? "))
                #     pennies = int(input("How many pennies? "))
                # except ValueError:
                #     print("Invalid value")
                #     continue
                have_money_sufficient = money_machine.make_payment(item.cost)

                if have_money_sufficient:
                    coffe_maker.make_coffee(item)
                    # print(f"Here is {money_machine.CURRENCY}{refunded_amount} in change.")
                    # print(f"Here is your {choice}. Enjoy!")            
            else:
                break
        elif choice == "report":
            money_machine.report()
            coffe_maker.report()
        elif choice == "off":
            exit()
        else:
            print("Wrong input.")
            continue


if __name__ == "__main__":
    main()




