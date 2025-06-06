last_char_of_string = "Hello"[-1]
print(last_char_of_string)

large_num_with_spacers = 123_456
print(large_num_with_spacers)

my_float = 12.34
print(my_float)

print(True)
print(False)

print(type(True))
print(type("String"))
print(type(123))
print(type(4.56))

print("abc".__len__())

# help(str.__len__)

print(("addition of these two ints is " + str(int("2")) + str(int("3"))))
print("addition of these two ints is " + str(bool("True")))
print("addition of these two ints is " + str(float("2.23")) + str(float("1.11")))
print("addition of these two ints is " + str(True) + str(2.23))

print("Number of letters in your name: " + str(len(input("Enter your name please: "))))

# Mathematical operations
print(1 + 2)
print(7 - 3)
print(7 * 3)
print(8 / 3)
print(9 // 3)
print(2 ** 3)

print(round(1.49))
print(round(1.5))
print(round(1.512, 2))

a = 1
a += 5
a -= 14
print(f"a is equal to {a}")

print("Welcome to the tip calculator!")
amt = input("How much was the final bill? ")
tip_percentage = input("What tip percentage would you like to give? ")
number_of_people = input("How many people would you like to split it between? ")
amt_per_person = float(amt) * (float(1) + (float(f"{tip_percentage}")/100)) / float(number_of_people)
print(f"Each person must pay: £{round(amt_per_person, 2)}")