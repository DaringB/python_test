"""
　　  ∧ _ ∧
　　 ( ˘ω˘ )　　起床！
　 　|　⊃ ⊃
　　 └-⊃～⊃
　　　
　　　｜｜　　　　　　　　
　 ＿ _　　／(＿＿_
／　 (＿＿＿_／　／

@version: Python3.6.5
@encoding: utf-8
@author: Misora
@createTime: 2018/11/22 0:29
"""
import sys
import os
import datetime
sys.path.append(os.path.abspath('.'))

from classes.c_Clothes import Clothes
from classes.c_Client import Client
from classes.c_Subscription import Subscription

def main(argv):
    client_1=Client("123", "Janet", "21 Tamp")
    client_1.addPayment(1000)
    cloth_1 = Clothes('107', 'Elliat', 7, 237)
    datetime_1 = datetime.datetime(2019,8,31)
    datetime_2 = datetime.datetime(2019,9,7)
    sub_1 = Subscription(datetime_1, client_1)
    print(sub_1)

    sub_1.requestClothes(datetime_2,cloth_1)
    print(sub_1)

    datetime_3 = datetime.datetime(2019,9,22)
    sub_1.returnClothes(datetime_3)
    print(sub_1)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
