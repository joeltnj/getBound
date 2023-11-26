# my_library_project/app/models/user.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"
