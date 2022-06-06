# class User:
#    pass
#
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "zhanma"  # pass new attribute "username" to user_1
#
# print(user_1.username)

# example:

class User:
    def __init__(self, user_id, username):  # constructor
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




user_1 = User("001", "zhanma")
user_2 = User("002", "qianlu")
print(user_1.id + " " + user_1.username + " " + str(user_1.followers))

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

