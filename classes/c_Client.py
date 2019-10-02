class Client:
    def __init__(self, clientID, name, address):
        self._clientID = clientID
        self._name = name
        self._address = address
        self._balance = 0

    @property
    def clientID(self):
        return self._clientID

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, newValue):
        self._address = newValue

    @property
    def balance(self):
        return self._balance

    def addPayment(self, amt):
        if amt > 0:
            self._balance += amt
            return True
        else:
            return False

    def makePayment(self, amt):
        if amt > 0 and (self._balance - amt) >= 0:
            self._balance -= amt
            return True
        else:
            return False

    def __str__(self):
        return "Id: {:8} Name: {:<8} Address: {:8} Payment due: ${:.2f}" \
            .format(self._clientID, self._name, self._address, self._balance)
