# Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
#
# Класс truck имеет дополнительный обязательный атрибут max_load.
#
# Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention», его реализацию сделать при
# помощи оператора super.
#
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load» и снова
# пауза 1 сек.
#
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
#
# метода move, после появления надписи «move» должна появиться надпись
#
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибута max_speed.
#
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.

import time


class auto:

    def __init__(self, brand, age, mark, weight='', color=''):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color

    def move(self):
        print('«move»')

    def stop(self):
        print('«stop»')

    def birthday(self):
        self.age += 1
        print(self.age)




class truck(auto):

    def __init__(self, max_load, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        super(truck, self).move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class car(auto):

    def __init__(self, max_speed, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super(car, self).move()
        print(f'«max speed is <{self.max_speed}>»')

    def stop(self):
        super(car, self).stop()



car1 = car(1000, 'f', 3, 'F')
truck1 = truck(200, 'w', 10, 'W', )

truck1.move()

truck1.load()

car1.move()
