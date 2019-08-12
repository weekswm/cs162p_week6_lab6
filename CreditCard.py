import math
from Person import Person

class CreditCard:
    '''Creates a credit card object

    attributes: firstName, lastName, address, cardNumber, creditLimit, balance
    '''

    def __init__(self, firstName = "", lastName = "", address = "", cardNumber = 0, creditLimit = 0, balance = 0):
        self.accountOwner = Person(firstName, lastName, address)
        self.cardNumber = cardNumber
        self.balance = balance
        self.creditLimit = creditLimit

    def getBalance(self):
        return self.balance

    def getCardNumber(self):
        return self.cardNumber

    def getOwnerName(self):
        return self.accountOwner.getFirstName() + " " + self.accountOwner.getLastName()

    def getAddress(self):
        return self.accountOwner.getAddress()

    def payBalance(self, moneyIn):
        if moneyIn >= 0:
            self.balance -= moneyIn
            return True
        else:
            #Payments must be non-negaAve values
            return False

    def makeCharge(self, moneyOut):
        if moneyOut <= 0:
            #Cannot charge a negative amount; that is a payment
            return False
        elif abs(moneyOut + self.balance) > self.creditLimit:
            #Cannot exceed credit limit
            return False
        else:
            self.balance += moneyOut
            return True
 
    def setCreditLimit(self, newLimit):
        if newLimit >= 0:
            self.creditLimit = newLimit
        else:
            print("New credit limit must be an amount greater than 0")
