import random

possible_words = ["epiphany", "lightning", "epiglottis", "chasm", "fluorescence"]
total_lives = 6

continue_game = True
random.shuffle(possible_words)

random_word = possible_words[0]

hidden_word = len(random_word) * "_"

while continue_game:
    index = -1
    print(f"You have {total_lives} lives left")
    print(f"Word progress is {hidden_word}")
    if total_lives == 0:
        print(f"You lost!! The word was {random_word}")
        continue_game = False

    elif total_lives >= 0:
        if not hidden_word.count("_") == 0:
            letter_guess = input("Pick a letter: ")
            if letter_guess in random_word:
                print("Correct!")
                for letter in random_word:
                    index += 1
                    if letter_guess == letter:
                        hidden_word = hidden_word[:index] + letter_guess + hidden_word[index + 1:]
            else:
                print("Incorrect")
                total_lives -= 1
        else:
            print(f"You win!! The word was {random_word}")
            continue_game = False