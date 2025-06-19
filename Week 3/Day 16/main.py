from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def start_coffee_machine():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    turn_off = False
    while not turn_off:
        order = input(f"What would you like? {Menu.get_items(menu)}")
        if order == "off":
            turn_off = True
        elif order == "report":
            money_machine.report()
        else:
            menu_item = menu.find_drink(order)
            if (coffee_maker.is_resource_sufficient(menu_item)):
                if money_machine.make_payment(menu_item.cost):
                    coffee_maker.make_coffee(menu_item)



start_coffee_machine()