




while True:

    user = input('Введите имя и возраст: ')

    base_name_age = user.split()

    if len(base_name_age) != 2:
        print('Вы ввели слишком много или слишком мало значений!')
        continue

    else:
        name = base_name_age[0]

        age = base_name_age[1]

    if age.isdigit() is False and name.isdigit() is True and int(name) > 0:
        age, name = name, age


    elif name.isdigit() is False and age.isdigit() is True and int(age) > 0:
        pass

    else:
        print('Ошибка')
        continue

    if int(age) < 10:
        print(f'“Привет, шкет #{name}#?”')

    elif int(age) < 18:
        print(f'“Как жизнь #{name}#?”')

    elif int(age) < 100:
        print(f'“Что желаете #{name}#?”')

    else:
        print(f'“#{name}#, вы лжете - в наше время столько не живут...”')

    end = input("Желаете выйти? (Д/Y): ")

    if end.upper() == 'Д' or end.upper() == 'Y' or end.upper() == 'Yes' or end.upper() == 'ДА':
        break

    else:
        continue
