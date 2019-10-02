class Clothes:
    def __init__(self, clothesID, brand, size, price):
        self._clothesID = clothesID
        self._brand = brand
        self._size = size
        self._price = price
        self._onLoan = False

    @property
    def clothesID(self):
        return self._clothesID

    @property
    def brand(self):
        return self._brand

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self._price

    @property
    def onLoan(self):
        return self._onLoan

    @onLoan.setter
    def onLoan(self, newValue):
        self._onLoan = newValue

    def __str__(self):
        return "Clothe Loan Id: {:8} Brand: {:<8} Size: {:<3} Price: ${:.2f} Out: {:3}" \
            .format(self._clothesID, self._brand, self._size, self._price, ["no", "yes"][self._onLoan])
