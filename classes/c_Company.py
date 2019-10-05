from classes.c_Clothes import Clothes
from classes.c_Client import Client
from classes.c_Subscription import Subscription

import datetime


class Company:
    def __init__(self):
        self._clothesList = []
        self._subList = []
        self._clientDic = {}  # { clientID : Client,...}

    def searchClient(self, clientID):
        for clientKey, client in self._clientDic.keys():
            if clientID == clientKey:
                return client
        return None

    def searchClothes(self, clothesID):
        for clothes in self._clothesList:
            if clothesID == clothes.clothesID:
                return clothes
        return None

    def searchSubByClienID(self, clientID):
        for sub in self._subList:
            if clientID == sub.client.clientID:
                return sub
        return None

    def addClient(self, clientID, name, address):
        if self.searchClient(clientID):
            return False
        else:
            self._clientDic[clientID] = Client(clientID, name, address)
            return True

    def addSub(self, client, startDate):
        if self.searchSubByClienID(client.clientID) is not None:
            return False
        elif client.makePayment(100):  # 会员费多少啊？ 醉了.....
            self._subList.append(Subscription(startDate, client))
            return True
        else:
            return False

    def addClothes(self, clothes):
        if self.searchClothes(clothes.clothesID) is None:
            return False
        else:
            self._clothesList.append(clothes)

    def cancelSub(self, clientID, cancelDate):
        client = self.searchClient(clientID)
        sub = self.searchSubByClienID(clientID)
        if client is None:
            pass
        elif client.balance < 0:  # 余额？
            pass
        elif sub is None:
            pass
        elif cancelDate < sub.startDate or cancelDate > sub.startDate + datetime.timedelta(weeks=2):
            pass
        else:
            self._subList.remove(sub)
            return True
        return False

    def returnClothes(self, clientID, returnClothes):
        sub = self.searchSubByClienID(clientID)
        if self.searchClient(clientID) is not None and sub is not None:
            return sub.returnClothes(datetime.date.today(), returnClothes)
        return False

    def requestClothes(self, clientID, requestDate, clothes):
        sub = self.searchSubByClienID(clientID)
        if clothes.onLoan:
            return False
        elif self.searchClient(clientID) is None or sub is None:
            return False
        else:
            return sub.requestClothes(requestDate, requestDate)

    def clothesStr(self):
        pass

    def availableClothesStr(self):
        pass

    def clientStr(self):
        pass

    def subStr(self):
        pass

    def __str__(self):
        return ""
