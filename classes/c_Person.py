class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_all(self):
        self._say_name()
        self._say_age()

    def _say_name(self):
        print('name is {}'.format(self.__name))

    def _say_age(self):
        if self.age > 18:
            print('age is {}\n'.format(self.__age))
        else:
            print('クソガキ！\n')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value