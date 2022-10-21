# Сделать программу в виде функций в которой нужно будет угадывать число.

import random

answer = ('YES', 'ДА', "Y", 'Д')



def game_random(user_try=3, end_game=0):
    while user_try != end_game:
        user = input(f'Угадай число от 1 до 3, количество попыток {user_try} : ')

        if user.isdigit() is False or 0 > int(user) > 4:
            print('Только числа от 1 до 3')

        elif int(user) == random.randint(0, 3):
            print('Вы угадали')
            choose = input('хотите начать закончить? (Y/Д): ')
            if choose.upper() == answer:
                break
            else:
                pass

        elif int(user) != random.randint(0, 3):
            print('Не угадали')
            user_try = int(user_try - 1)


game_random()
