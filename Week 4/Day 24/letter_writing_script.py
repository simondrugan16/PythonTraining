with open("Week 4/Day 24/Friends/friends.txt") as file:
    with open("Week 4/Day 24/Letters/letter_template.txt") as letter_template:
        letter_template = letter_template.read()
        friends_names = file.read()
        for friend_name in friends_names.split("\n"):
            with open(f"Week 4/Day 24/Letters/Letters to friends/party_invite_for_{friend_name}.txt", mode="w") as new_file:
                new_file.write(letter_template.replace("{name}", friend_name))
