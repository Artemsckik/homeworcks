# Написать программу, которая состоит из вечного цикла ожидающего ввод числа или одно из значений: "выход", "exit",
# "quit", "e" или "q" в любом регистре. При вводе одного из этих значений происходит выход из вечного цикла. При
# любом другом вводе вызывается отдельная функция которая умеет распознавать введённые числа. Сама функция ничего не
# распечатывает, она возвращает строку, типа: "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не
# корректное число: Erdf"
#
# Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.
#
# Функция на вход принимает строку из ввода из вечного цикла. Анализирует её исключительно методом .isdigit() и
# другими методами строк, без доп. библиотек и переводит строку в число, если это возможно.
#
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же распознаёт десятичные дроби как с
# точкой, так и с запятой.
#
# Функция возвращает строку в которой описывается какое число введено - отрицательное или положительно,
# целое или дробное и выводит его или же сообщает, что введено не корректное число.
#
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля
#
#
#
# Примеры:
#
# -6,7 → Вы ввели отрицательное дробное число: -6.7
#
# 5 → Вы ввели положительное целое число: 5
#
# 5.4r → Вы ввели не корректное число: 5.4r
#
# -.777 → Вы ввели отрицательное дробное число: -0.777

while True:
    user1 = input('Введите число ')
    if user1.upper() == 'Q' or user1.upper() == "ВЫХОД" or user1.upper() == "QUIT" or user1.upper() == "E" \
            or user1.upper() == "EXIT":
        break


    def numbers():  # Сама функция

        user = user1
        n = len(user)
        v = list(user)
        number = []
        sings = []
        sing2 = []


        q = 0
        while q != n:
            if v[q].isnumeric():
                number.append(v[q])
                q += 1
            else:
                sings.append(v[q])
                sing2.append(v[q])
                q += 1


        counts = []

        def count():  # Подсчёт элементов в списке
            h = 0
            sing = ''
            if '.' in user:
                sing = '.'
            elif ',' in user:
                sing = ','
            q += 1
            while True:
                if not sing in sings:
                    break

                else:
                    sings.remove(sing)
                    q += 1

            counts.append(q)
        if len(number) == 0:
            print(f'{user} → Вы ввели не корректное число: {user}')
        elif user[0] == '-':  # Блок отрицательных чисел
            count()
            if counts[0] > 2 or len(sings) > 2:
                print(f'{user} → Вы ввели не корректное число: {user}')
            elif user[1] == ',':
                user2 = user.split(sep=',')
                print(f'{user} → Вы ввели отрицательное дробное число: {user2[0] + "0." + user2[1]}')
            elif user[1] == '.':
                user2 = user.split(sep='.')
                print(f'{user} → Вы ввели отрицательное дробное число: {user2[0] + "0." + user2[1]}')
            elif '.' in user:
                print(f'{user} → Вы ввели отрицательное дробное число: {user}')
            elif ',' in user:
                user2 = user.split(sep=',')
                print(f'{user} → Вы ввели отрицательное дробное число: {user2[0] + "." + user2[1]}')
            elif len(sings) == 1:
                print(f'{user} → Вы ввели отрицательное целое число: {user}')
            else:
                print(f'{user} → Вы ввели не корректное число: {user}')
        elif ',' in user or '.' in user:  # Блок положительных дробных чисел
            count()
            if counts[0] > 2 or len(sing2) > 1:
                print(f'{user} → Вы ввели не корректное число: {user}')
            elif user[0] == ',':
                user2 = user.split(sep=',')
                print(f'{user} → Вы ввели положительное дробное число: 0.{user2[1]}')
            elif user[0] == '.':
                print(f'{user} → Вы ввели положительное дробное число: 0{user}')
            elif ',' in user:
                user2 = user.split(sep=',')
                print(f'{user} → Вы ввели положительное дробное число: {user2[0] + "." + user2[1]}')
            elif len(sing2) == 1:
                print(f'{user} → Вы ввели положительное дробное число: {user}')
            else:
                print(f'{user} → Вы ввели не корректное число: {user}')
        elif len(sings) == 0:
            print(f'{user} → Вы ввели положительное целое число: {user}')
        else:
            print(f'{user} → Вы ввели не корректное число: {user}')


    numbers()