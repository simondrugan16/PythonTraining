
try:
    age = int(input("How old are you? "))
except ValueError:
    print("This is the wrong type of input. Try again with a number")
    age = int(input("How old are you? "))

if age >= 18:
    print("You can legally drink alcohol in the UK!")