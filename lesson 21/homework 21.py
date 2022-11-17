# Создать родительский класс auto, у которого есть атрибуты:
#
# brand, age, cоlor, mark и weight.
#
# А так же методы: move, birthday и stop.
#
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
#
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class auto:

    def __init__(self, brand, age, mark, weight='',color=''):
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


auto1 = auto('ferari', 3, 'Ferrari NV')

auto1.move()
auto1.stop()
auto1.birthday()

