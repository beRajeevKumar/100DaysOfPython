class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


# Constructors

user_1 = User("001", "Rajeev Kumar")
print(user_1.id, user_1.username, user_1.followers)
