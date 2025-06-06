print("Welcome to the roller coaster!!")
height = int(input("What is your height in centi metres? "))

if height > 120:
    print("Get on and have fun!")
else:
    print("Sorry you have to grow a lil bit")

print(100 % 33) # % gets the remainder

print("Enter a number to check if it is even or odd!")
number = int(input("Enter your number: "))

if number % 2 == 1:
    print("Your number is odd")
else:
    print("Your number is even")

print("This ride costs a fiver per person mate")
height = int(input("Enter a different height for this other ride? "))
bill = 0
ticket = 5
if height <= 120:
    print("Not big enuf! No ticket purchased")
    bill += 0
elif height <= 140:
    print("You can ride with a parent or guardian. Two tickets purchased!")
    bill += 2 * ticket
else:
    print("Jobs a goodun, fire away! One ticket purchased")
    bill += ticket

wants_pic = input("Would you like a picture? 'y' or 'n' ")

if wants_pic == 'y':
    bill += 7.5

print(f"Total bill is £{bill}")
