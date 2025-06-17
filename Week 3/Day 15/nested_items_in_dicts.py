menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 10
        },
        "cost": 2.7
    },
    "mocha": {
        "ingredients": {
            "water": 40,
            "milk": 30,
            "chocolate": 50,
            "coffee": 10
        },
        "cost": 4.5
    }
}

print(menu["espresso"])
print(menu["espresso"]["cost"])
print(menu["espresso"]["ingredients"]["coffee"])
print(menu["mocha"]["ingredients"])
## print(menu[0][0])