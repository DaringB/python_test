import datetime
import sys

class Client:
    def __init__(self,cid,name,address):
        self._id = cid
        self._name = name
        self._address= address
        self._balance = 0      
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self,newAddress):
        self._address=newAddress
        
    def addPayment(self,amt):
        if amt>0:
            self._balance += amt
            return True
        else:
            return False
        
    def makePayment(self,amt):
        if amt>0 and self._balance>0:
            self._balance-=amt
            return True
        else:
            return False
        
    def __str__(self):
        return "Id: {} Name: {} Address: {} Payment due: ${:.2f}"\
            .format(self._id,self._name,self._address,self._balance)

class Clothes:
    def __init__(self,clothId,brand,size,price):
        self._clothId=clothId
        self._brand=brand
        self._size=size
        self._price=price
        self._loanStatus=False
    
    def __str__(self):
        if self._loanStatus == False:
            self._loanStatus="no"
        else:
            self._loanStatus="yes"
        return "Clothe Loan Id: {} Brand: {} Size: {} Price: ${:.2f} Out: {}"\
            .format(self._clothId,self._brand,self._size,self._price,self._loanStatus)
            
    @property
    def clothId(self):
        return self._clothId
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
    def loanStatus(self):
        return self._loanStatus
    @loanStatus.setter
    def loanStatus(self,newStatus):
        self._loanStatus=newStatus        

class subscription:
    _nextId=1
    def __init__(self, startDate, client):
        self._subscriptionId = "{}".format(subscription._nextId)
        subscription._nextId+=1
        self._subRate = 69
        self._startDate = startDate
        self._client = client
        self._clothes = Clothes
        self._returnDate = None
        self._deliverDate = None
           
    def getSubscriptionRate(self):
        return self._subRate

    @property
    def subscriptionId(self):
        return self._subscriptionId
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
    def clothes(self,newClothes):
        self._clothes = newClothes
    @property
    def returnDate(self):
        return self._returnDate
    @returnDate.setter
    def returnDate(self,newReturnDate):
        self._returnDate=newReturnDate
        
    @property
    def deliverDate(self):
        return self._deliverDate
    @deliverDate.setter
    def deliverDate(self,newDeliverDate):
        self._deliverDate=newDeliverDate
        
    def returnClothes(self,returnDate):
        if self._deliverDate>returnDate or self._clothes==None:
            return False
        else:
            Clothes.loanStatus = False
            self._clothes =None
            self._returnDate = returnDate
            return True
        
    def requestClothes(self,requestDate,clothes):
            delta = datetime.timedelta(1)
            self._deliverDate = requestDate+delta
            Clothes._loanStatus = True
            self._clothes = clothes
            return True
        
    def __str__(self):
        
        newUser = "{}".format(self._client)
        if subscription.returnClothes == False:
            return"Subscription Id: {} Start Date: {}\n"\
                .format(self.subscriptionId, self._startDate.strftime("%A, %d %B %Y"))\
                +newUser+ "\nNo outstanding clothes."
        elif subscription.returnClothes == True:
            return"Subscription Id: {} Start Date: {}\n"\
                .format(self.subscriptionId, self._startDate.strftime("%A, %d %B %Y"))\
                +newUser+ "No outstanding clothes"+"Returned: {}".format(self._returnDate.strftime("%A, %d %B %Y"))
        else:
            return "Subscription Id: {} Start Date: {}\n".format(self.subscriptionId, self._startDate.strftime("%A, %d %B %Y"))\
                +newUser\
                +"\nClothes Loaned {}".format(self._clothes)\
                + "Delivered: {}".format(self._deliverDate.strftime("%A, %d %B %Y")) 


def main(argv):
    c1=Client("123", "Janet", "21 Tamp")
    c1.addPayment(69)
    print(c1)
    C1= Clothes("107", "Elliat", 7, 237)
    print(C1)
    print("=============")
    d1 = datetime.datetime(2019,8,31)
    d2 = datetime.datetime(2019,9,7)
    s1 = subscription(d1,c1)
    s1.requestClothes(d2,C1)
    print(s1)

if __name__ == '__main__':
    sys.exit(main(sys.argv))