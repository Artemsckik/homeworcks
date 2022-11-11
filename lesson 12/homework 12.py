# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
#
# Подсказка:
#
# from datetime import datetime
#
# time = datetime.now()

from datetime import datetime


def decorator(func):
    start = datetime.now()
    func()
    finish = datetime.now()
    print(finish - start)


@decorator
def user():
    print('1')
    number = int(input('Введите число: '))


@decorator
def user2():
    print('2')
    input()
