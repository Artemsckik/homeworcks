# Создать программу-калькулятор в виде класса и несколько методов, как минимум сложение, вычитание, деление, умножение,
# возведение в степень и извлечение квадратного корня.
#
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
#
# Создать своё исключение, к примеру возведение в отрицательную степень.
import math


class calculated:

    def __init__(self, x, y=0):
        try:
            self.x = int(x)
            self.y = int(y)
        except Exception:
            print('Ошибка')

    def plus(self):
        if self.x < 0:
            raise Exception('Так не чесно')
        try:
            result = self.x + self.y
            print(result)
        except Exception as e:
            print(e)

    def minus(self):
        try:
            result = self.x - self.y
            print(result)
        except Exception:
            print(Exception)

    def divide(self):
        try:
            result = self.x / self.y
            print(result)
        except ZeroDivisionError:
            print('ошибка')

    def multiply(self):
        try:
            result = self.x * self.y
            print(result)
        except Exception:
            print(Exception)

    def degree(self):
        try:
            result = self.x ** self.y
            print(result)
        except Exception:
            print(Exception)

    def sqrt(self):
        if self.x < 0:
            raise Exception('так дела не делаются')
        try:
            result = math.sqrt(self.x)
            print(result)
        except Exception as e:
            print(e)


while True:
    print('-' * 30)
    print('-' * 10, 'Calculated', '-' * 10)
    print('-' * 30)
    x = input('Число 1: ')
    user2 = input('Введите действие: ')
    y = input('Введите число 2: ')
    a = calculated(x, y)
    try:
        if '+' in user2:
            a.plus()
        elif '-' in user2:
            a.minus()
        elif user2[0] == '/':
            a.sqrt()
        elif ':' in user2:
            a.divide()
        elif '*' in user2:
            a.multiply()
        elif '**' in user2:
            a.degree()
        else: print('Ошибка')
    except Exception as e:
        print(e)

    finally:
        end = input('Хотите закончить? ')
        if 'ДА' in end.upper():
            break
