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
@createTime: 2018/11/27 21:50
"""
import sys


class MyString:
    def __init__(self, value=""):
        self.__string_ = value

    def do_string(self):
        v = "@_@".join(self.__string_)
        print(v)


def main(argv):
    mystring = MyString("misoraaa")
    mystring.do_string()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
