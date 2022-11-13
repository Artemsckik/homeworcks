# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
#
# Создать файл и записать в него первые 2 строки и закрыть файл.
#
# Затем открыть файл на редактирование и записать оставшиеся 2 строки.
#
# В итоге файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

with open('file txt', 'w') as file_sources:
    user = input('Введите слово: ')
    user2 = input('Введите слово: ')
    file_sources.write(user + '\n')
    file_sources.write(user2 + '\n')

with open('file txt', 'a') as file_sources:
    user = input('Введите слово: ')
    user2 = input('Введите слово: ')
    file_sources.write(user + '\n')
    file_sources.write(user2 + '\n')



