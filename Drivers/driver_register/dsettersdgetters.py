class DriverSetGet():
    def __init__(self, name=None, licenseNo=None,email=None,password=None,address=None):
        self.name = name
        self.licenseNo = licenseNo
        self.email = email
        self.password = password
        self.address = address
    def getName(self):
        return self.name

    def getLicenseNo(self):
        return self.licenseno

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def getAddress(self):
        return self.address

    def setName(self, name):
        self.name = name

    def setLicenseNo(self, licenseNo):
        self.licenseno = licenseNo

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    def setAddress(self, Address):
        self.Address = Address


class String1():
    def __str__(self):
        return str(self.name + ", " + self.licenseNo + "," + self.email + "," + self.password + "," + self.address)