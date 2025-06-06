
def my_function():
    print("Hello world")

number_time_to_run = 6

while number_time_to_run > 0:
    my_function()
    print(f"Num times left to run is {number_time_to_run}")
    number_time_to_run -= 1

my_bool = False

while not my_bool:
    print(f"We false, see: {my_bool}")
    my_bool = True