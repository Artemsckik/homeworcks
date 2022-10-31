# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”, если нет - то “не чётное”.

def even():
    while True:
        user = input('Введите число ')
        if not user.isdigit():
            continue
        else:
            user = [int(user)]
        resault = filter(lambda x: x % 2 != 0, user)
        resault = list(resault)
        if len(resault) == 0:
            print(f'Ваше число {user} чётное!')
        else:
            print(f'Ваше число {user} не чётное!')

        end = input('хотите выйти? y/yes: ')
        if end.upper() == 'YES':
            break
        else:
            continue


even()
