from classes.c_Clothes import Clothes
from classes.c_Client import Client
import datetime


class Subscription:
    _nextID = 1
    _subscriptionRate = 69

    def __init__(self, startDate, client):
        self._subscriptionID = str(Subscription._nextID)
        Subscription._nextID += 1
        self._startDate = startDate
        self._client = client
        self._clothes = None
        self._returnedDate = None
        self._deliveredDate = None

    @classmethod
    def getSubscriptionRate(cls):
        return Subscription._subscriptionRate

    @property
    def subscriptionId(self):
        return self._subscriptionID

    @property
    def startDate(self):
        return self._startDate

    @property
    def client(self):
        return self._client

    @property
    def clothes(self):
        return self._clothes

    @clothes.setter
    def clothes(self, newValue):
        self._clothes = newValue

    @property
    def returnedDate(self):
        return self._returnedDate

    @returnedDate.setter
    def returnDate(self, newValue):
        self._returnedDate = newValue

    @property
    def deliverDate(self):
        return self._deliveredDate

    @deliverDate.setter
    def deliverDate(self, newValue):
        self._deliveredDate = newValue

    def returnClothes(self, returnDate):
        if self._clothes is None or \
           returnDate < self.deliverDate:
            """
            this return ge mao。。。
            """
            return False
        else:
            """
            now you can return
            """
            self._clothes.onLoan = False
            self._clothes = None
            self._returnedDate = returnDate
            return True

    def requestClothes(self, requestDate, clothes):
        if self._clothes is not None or \
                clothes.onLoan is True or \
                requestDate < self._startDate or \
                (self._returnedDate is not None and requestDate < self._returnedDate):
            return False
        else:
            self._deliveredDate = requestDate + datetime.timedelta(days=1)
            clothes.onLoan = True
            self._clothes = clothes
            return True

    def __str__(self):
        if self._returnedDate is None and \
                self._clothes is None:

            return "Subscription Id: {} Start Date: {} \n{} \nNo outstanding clothes.\n" \
                .format(self._subscriptionID,
                        self._startDate,
                        self._client)

        elif self._returnedDate is not None and \
                self._clothes is None:

            return "Subscription Id: {} Start Date: {} \n{} \nNo outstanding clothes   Returned: {}\n" \
                .format(self._subscriptionID,
                        self._startDate.strftime("%d %B %Y"),
                        self._client,
                        self._returnedDate.strftime("%d %B %Y"))

        elif self._clothes is not None:

            return "Subscription Id: {} Start Date: {} \n{} \nClothes Loaned {} Delivered: {}\n" \
                .format(self._subscriptionID,
                        self._startDate.strftime("%d %B %Y"),
                        self._client,
                        self._clothes,
                        self._deliveredDate.strftime("%d %B %Y"))
