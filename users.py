users = []

class Users():
    def __init__(self, username, password, role):
        self.user_id = len(users)+1
        self.username = input("Choose a username> ")
        self.password = input("provide a password> ")
        self.role = input("Enter role> ")

    def signup(self):
        user = {
            'userid':self.user_id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
        users.append(user)
        print(user)
