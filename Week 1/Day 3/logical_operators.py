x = 1
y = 2

if x == 1 or y == 3:
    print("X = 1 OR Y = 3")

if x == 1 and y == 3:
    print("THIS WILL NEVER PRINT (unless change y)")

if not x == 1 or not y == 3:
    print("This should print since the not operator is used")

if not x == 2 and not y == 1:
    print("This should print since the not operator is used and both conditions are false")
