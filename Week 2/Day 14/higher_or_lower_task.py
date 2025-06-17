import random

def pick_new_person(dict_of_people):
    new_person, number_followers = random.choice(list(dict_of_people.items()))
    dict_of_people.pop(new_person)
    return (new_person, number_followers)

def is_correct(number_followers, new_number_followers, original_has_more):
    result = (number_followers >= new_number_followers and original_has_more == "y") or (new_number_followers >= number_followers and not original_has_more == "y")
    return result

def play_game(dict_of_people):
    original_person, number_followers = random.choice(list(dict_of_people.items()))
    dict_of_people.pop(original_person)
    score_counter = 0
    _continue = True
    while _continue:
        new_person, new_number_followers = pick_new_person(dict_of_people)
        original_has_more = input(f"Who has more followers? {original_person} ('y') or {new_person} ('n')? ")
        if is_correct(number_followers, new_number_followers, original_has_more):
            print(f"Congrats you were correct!\n{original_person} had {number_followers} followers\n{new_person} had {new_number_followers} followers")
            score_counter += 1
            if original_has_more == "n":
                original_person = new_person
                number_followers = new_number_followers
        else:
            print(f"Oh no you were wrong...\n{original_person} had {number_followers} followers\n{new_person} had {new_number_followers} followers")
            _continue = False
    print(f"You finished with {score_counter} point(s)!")


dict_of_people = {
    "Taylor Swift": 285,
    "Cristiano Ronaldo": 630,
    "Kim Kardashian": 364,
    "Lionel Messi": 520,
    "Selena Gomez": 429,
    "Dwayne Johnson": 395,
    "Ariana Grande": 380,
    "Kylie Jenner": 400,
    "Beyoncé": 320,
    "Justin Bieber": 290,
    "Zendaya": 190,
    "Drake": 150,
    "Billie Eilish": 115,
    "Rihanna": 150,
    "Emma Watson": 75,
    "Chris Hemsworth": 115,
    "Lady Gaga": 58,
    "Tom Holland": 68,
    "Nicki Minaj": 230,
    "Shakira": 160
}

play_game(dict_of_people)