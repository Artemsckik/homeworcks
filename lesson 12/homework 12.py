# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
#
# Подсказка:
#
# from datetime import datetime
#
# time = datetime.now()

from datetime import datetime


def decorator(func):
    def time():
        start = datetime.now()
        func()
        finish = datetime.now()
        print(finish - start)
    return time


@decorator
def user():
    print('1')
    input('Введите число: ')


@decorator
def user2():
    print('2')
    input()

user()
user2()
