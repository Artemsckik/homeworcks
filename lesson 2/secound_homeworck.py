# Програма запрашивает строку, 2 строки, одна состоит из чётных символов, 2 выводит введёную строку в
# обратной последовательности
# 1 вариант

a = input()

print(2, 4, 6 , 8)

print(a[::-1])

# 2 вариант с проверкой строки и выводом

def cheaker():
    try:
        user = input('Введите число: ')

        if int(user) % 2 == 0:
            print(user)
            print(user[::-1])
        else: print('Число не чётное но вот оно в обратной последовательности', user[::-1])
    except:
        print(user[::-1].upper())
cheaker()

