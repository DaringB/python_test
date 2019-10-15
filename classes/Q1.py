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
        return "Id: {} Name: {} Address: {} Payment due: ${:.2f}" \
            .format(self._clientID, self._name, self._address, self._balance)


    
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
        return "Id: {} Brand: {} Size: {} Price: ${:.2f} Out: {}" \
            .format(self._clothesID, self._brand, self._size, self._price, ["no", "yes"][self._onLoan])


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
            return False
        else:
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
                        self._startDate.strftime("%d %B %Y"),
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
                
                
class Company:
    def __init__(self):
        self._clothesList = []
        self._subList = []
        self._clientDict = {}
    
    def searchClient(self, clientID):
        for clientKey,client in self._clientDict.items():
            if clientID==clientKey:
                return client
        return False
    def searchClothes(self,clothesID):
        for CID in self._clothesList:
            if CID == clothesID:
                return CID
        return False
    def searchSubscription(self,clientID):
        for sub in self._subList:
            if clientID == sub:
                return sub
        return False
    
    def addClient(self, clientID, name, address):
        if clientID not in self._clientDict:
            self._clientDict[clientID] = Client(clientID, name, address)
            return True
        else:
            return False   
    def addClothes(self,clothes):
        c = self.searchClothes(clothes)
        if c == False:
            self._clothesList.append(clothes)
            return True
        else:
            return False
    def addSubscription(self, clientId, startDate):
        if self.searchSubscription(clientId) is not False:
            return False
        elif self.searchClient(clientId): 
            sub = Subscription(startDate, self.searchClient(clientId))
            self.searchClient(clientId).makePayment(sub.getSubscriptionRate())
            self._subList.append(sub)
            return True
        else:
            return False

    def cancelSub(self, clientID, cancelDate):
        c = self.searchClient(clientID)
        s = self.searchSubscription(clientID)
        sd = self.searchSubscription(clientID).startDate()
        t = cancelDate-sd
        if c == None or Client(clientID).balance>0 or s == None or sd<cancelDate or t >28:
            return False
        else:
            self._subList.remove(clientID)
            return True
            
    def returnClothes(self, clientID, returnDate):
        c = self.searchClient(clientID)
        if c not in self._clientDict.keys() or c not in self._subList:
            return False
        else:
            return Subscription.returnClothes(returnDate)
            
    def requestClothes(self, clientID, requestDate, clothes):
        c = self.searchClothes(clothes)
        cid = self.searchClient(clientID)
        sub = self.searchSubscription(clientID)
        if c != None:
            if c.onLoan()==True:
                return False
        elif c == None:
            return False
        elif cid == None:
            return False
        elif sub == None:
            return False
        else:
            return Subscription.requestClothes(requestDate, clothes)

    def clientStr(self):
        msg = "Clients:\n"
        for c in self._clientDict.keys():
            msg+="{}\n".format(self._clientDict[c])
        return msg                
    def clothesStr(self):
        msg = "Clothes:\n"
        for c in self._clothesList:
            msg+="{}\n".format(c)
        return msg
    def availableClothesStr(self):
        msg = "Available Clothes are:\n"
        for c in self._clothesList:
            if c.onLoan()==False:
                msg+="{}\n".format(c)
        return msg
    def subStr(self):
        msg="Subscription:\n"
        for s in self._subList:
            msg+="{}\n".format(s)
        return msg

def main():
    client = Client("123","Janet","21 Tampines West Road")
    cloth1 = Clothes("34","Charm",7,147)
    cloth2 = Clothes("91","Elliatt",6,287)
    cloth3 = Clothes("104","Juillet",6,214)
    cloth4 = Clothes("107","Elliatt",7,237)
    cloth4.onLoan=True
    cloth5 = Clothes("115","Juillet",6,253)
    cloth6 = Clothes("123","Suncoo",6,194)
    date1 = datetime.datetime(2019,8,31)

    
    company = Company()
    company.addClient(client.clientID,client.name,client.address)
    company.searchClient(client.clientID).addPayment(69)
    company.addClothes(cloth1)
    company.addClothes(cloth2)
    company.addClothes(cloth3)
    company.addClothes(cloth4)
    company.addClothes(cloth5)
    company.addClothes(cloth6)
    company.addSubscription(client.clientID,date1)
    print("Test")
    print(company.clientStr())
    print(company.clothesStr())
    print(company.subStr())

    
main()
        
        


    

    