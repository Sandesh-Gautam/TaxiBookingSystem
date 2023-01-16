class LoginSetGet():
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def getEmail(self):
        return self.__email
    def getPassword(self):
        return self.__password
    def setEmail(self, email):
        self.__email = email
    def setPassword(self, password):
        self.__password = password

class String1():
    def __str__(self):
        return str(self.__email + ", " + self.__password)