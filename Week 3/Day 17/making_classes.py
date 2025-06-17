class User:
    def __init__(self, friends, user_id):
        self.friends = friends
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(5, "001")
user_1.enemies = 100

user_2 = User(9, "002")

print(f"User 1 enemies: {user_1.enemies}")

print(f"User 1 id: {user_1.id}")
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")

print("////////////")

print(f"User 2 id: {user_2.id}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")

print("////////////")

user_1.follow(user_2)
print("User 1 followed user 2")

print(f"User 1 id: {user_1.id}")
print(f"User 1 followers: {user_1.followers}")
print(f"User 1 following: {user_1.following}")

print("////////////")

print(f"User 2 id: {user_2.id}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 2 following: {user_2.following}")