
def add(n1, n2):
    return n1 + n2

def calculator(n1, n2, func):
    return func(n1, n2)

print(calculator(2, 5, add))