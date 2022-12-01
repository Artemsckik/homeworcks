# Создайте свой произвольный класс и в нём помимо обычных методов и атрибутов создайте несколько
# статических методов и методов класса.
#
# Продемонстрируйте их работу.

class dog:
    def __init__(self, money):
        self.money = money

    def sey(self):
        print('woof')
        print(self.money)

    @staticmethod
    def actions():
        print('dog say')

    @staticmethod
    def H_H():
        print('H_H')

a = dog(1000)

a.sey()
a.actions()
a.H_H()