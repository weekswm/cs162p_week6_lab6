class Person:
    '''Creates a person oject

    attributes: firstName, lastName, address
    '''

    #initialize Person class with first, last, and address
    def __init__(self, firstName = "", lastName = "", address = ""):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address

    #Getters and Setters for Person Class
    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.firstName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getAddress(self):
        return self.address

    def setAddress(self, newAddress):
        self.address = newAddress
    #End Getters and Setters
