users = []

class Users():
    def __init__(self, username, password, role):
        self.user_id = len(users)+1
        self.username = input("Choose a username> ")
        self.password = input("provide a password> ")
        self.role = input("Assign role> ")

    def signup(self):
        user = {
            'userid':self.user_id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
        users.append(user)
        print(user)

    def login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        role = input("Enter your role: ")
        for user in users:
            if username == user['username'] and passsword == user['password'] and role == user['role']:
                print("Successful login")
            else:
                print('Incorrect login!')
