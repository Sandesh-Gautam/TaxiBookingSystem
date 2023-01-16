class CustomerSetGet():
    def __init__(self, name=None, phone=None,email=None,password=None,address=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.name = name

    def setPhone(self, Phone):
        self.Phone = Phone

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    def setAddress(self, Address):
        self.Address = Address


class String1():
    def __str__(self):
        return str(self.name + ", " + self.phone + "," + self.email + "," + self.password + "," + self.address)