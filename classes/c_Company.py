from classes.c_Clothes import Clothes
from classes.c_Client import Client
from classes.c_Subscription import Subscription

class Company:
    def __init__(self):
        self._clothesList = []
        self._subList = []
        self._clientDic = {}    #{ clientID : Client,...}
    
    def searchClient(self, clientID):
        for clientKey,client in self._clientDic.keys():
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
        if clientID not in self._clientDic:
            self._clientDic[clientID] = Client(clientID, name, address)
            return True
        return False

    def addSub(self, client, startDate):
        for sub in self._subList:
            if client.clientID == sub.client.clientID:
                return False
        
        self._subList.append(Subscription(startDate, client))

    def addClothes(self, clothes):
        pass
    def cancelSub(self, clientID, cancelDate):
        pass
    def returnClothes(self, clientID, returnClothes):
        pass
    def requestClothes(self, clientID, requestDate, clithes):
        pass
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