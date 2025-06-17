
def greet(name: str, location: str):
    print(f"hello {name} of {location}")
    print(f"welcome {name}")
    print(f"in {name}")

greet(location= "Winterfell", name= "Simon")

def calculate_love_score(name1: str, name2: str):
    name1 = name1.upper()
    name2 = name2.upper()
    true_in_n1 = name1.count("T") + name1.count("R") + name1.count("U") + name1.count("E")
    love_in_n1 = name1.count("L") + name1.count("O") + name1.count("V") + name1.count("E")
    true_in_n2 = name2.count("T") + name2.count("R") + name2.count("U") + name2.count("E")
    love_in_n2 = name2.count("L") + name2.count("O") + name2.count("V") + name2.count("E")
    print(str(true_in_n1 + true_in_n2) + str(love_in_n1 + love_in_n2))
    
    
calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")

print(ord("z"))
print(ord("{"))