
def add(first_num: float, second_num: float):
    return first_num + second_num

def subtract(first_num: float, second_num: float):
    return first_num - second_num

def multiply(first_num: float, second_num: float):
    return first_num * second_num

def divide(first_num: float, second_num: float):
    return first_num / second_num

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def continue_calc(result: float):
    _continue = True
    while _continue:
        if input("Would you like to continue, 'y' or 'n'? ") == "n":
            _continue = False
        else:
            operation = input("What operation would you like to perform? \n+\n-\n*\n/\n")
            next_num = float(input("What is the next number? "))
            result = operations[operation](result, next_num)
            print(f"The current result is {result}!")
    print(f"The final result is: {result}!")
    return result

def start_calc():
    first_num = float(input("What is the first number? "))
    operation = input("What operation would you like to perform? \n+\n-\n*\n/\n")
    second_num = float(input("What is the second number? "))
    result = operations[operation](first_num, second_num)
    print(f"The current result is {result}!")
    continue_calc(result)

start_calc()