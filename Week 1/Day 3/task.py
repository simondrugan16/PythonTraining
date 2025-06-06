if input("left or right? ") == "right":
    print("Game over.")
else:
    if input("swim or wait? ") == "swim":
        print("Game over.")
    else:
        door_choice = input("which door (red, blue or yellow)? ")
        if door_choice == "red":
            print("Game over.")
        elif door_choice == "blue":
            print("Game over.")
        else:
            print("You win!!")
