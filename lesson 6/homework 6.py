# Сделать программу в виде функций в которой нужно будет угадывать число.

import random


def game_choose():

    user_try = 3

    score = 0

    while user_try != 0:
        user = input(f'угадайте число от 1 до 3, ваше число попыток {user_try}, ваши очки {score} ')
        game_random = random.randint(1, 3)
        if not user.isdigit():
            print('Только числа')
            continue
        elif int(user) < 1 or int(user) > 3:
            print('Только числа от 1 до 3')
            continue
        elif user_try == game_random:
            print('Вы угадали')
            print(f'Число {game_random}')
            user_try = user_try - 1
            score = score + 1
        elif user_try != game_random:
            print('Не угадали')
            user_try = user_try - 1
            print(f'Число {game_random}')



game_choose()
