def add_but_mainly_1(a: int, b: int = 1):
    return a + b

print(add_but_mainly_1(a = 4))

def add_args(*args: int):
    counter = 0
    for arg in args:
        counter += arg
    return counter

print(add_args(100, 2, 3, 4, 5))

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

print(calculate(5, add = 3, multiply = 5))

class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"]
        self.model = kwargs.get("model")

my_car = Car(make = "Toyota")

print(my_car.make, my_car.model)