import random

number_of_lives = 5
def play_game():
    global number_of_lives
    random_number = random.randint(1, 100)

    while number_of_lives > 0:
        print (f"You have {number_of_lives} lives")
        guess = int(input("Pick a number betwixt 1 incl and 100 incl. "))
        if guess > random_number:
            number_of_lives -= 1
            print("You need to guess lower...")
        elif guess < random_number:
            number_of_lives -= 1
            print("You need to guess higher...")
        else:
            print("Congrats... U got it i guess..")

play_game()