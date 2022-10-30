# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.


a = [1, 2, 2, 2, 3, 'lol']


def count(amount=0):
    b = a

    element = input('введите элемент: ')

    if not element.isdigit():
        ...
    else:

        element = int(element)
    while True:

        if not element in b:
            break

        else:
            b.remove(element)
            amount = amount + 1

    print(f'Ваш элемент {element}, количество элемента в списке {amount} ')


count()
