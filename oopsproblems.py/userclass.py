class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password    # private variable

    def login(self, password):
        if password == self.__password:
            print("Login successful!")
        else:
            print("Incorrect password!")


# Example
u = User("Akhila", "1234")
u.login("1234")      # correct
u.login("9999")      # wrong
