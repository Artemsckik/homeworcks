# Используя input() ввести предложение состоящее из двух слов. Создать 2 переменные и в каждую
# записать по 1 введённому слову используя методы строк. Создать новую переменную 3-мя разными
# способами форматирования (фактически 3 переменные), которая бы состояла из введённых слов в
# обратном порядке, первое слово должно состоять только из больших букв, а второе с первой
# заглавной буквы и остальных маленьких. В начале предложения должен быть восклицательный
# знак, а в конце вопросительный.
# Используя только атрибуты функции print() вывести первоначальную строку и получившиеся
# разными способами форматирования через разделитель "<<<>>>", вывод сделать в файл.


file_sourse = open('file.txt', 'w')

user_name = input('Введите имя и фамилию ')

list_name_surname = user_name.split()


name = list_name_surname[0][::-1].upper()

surname = list_name_surname[1][::-1].capitalize()

print('',' Ваше имя - %s, Ваша фамилия - %s ' %(name,surname), end='! >>>>', sep='<<<< ? ', file=file_sourse)
print(file=file_sourse)
print('',' Ваше имя - {}, Ваша фамилия - {} '.format(name,surname) , end='! >>>>', sep='<<<< ? ',file=file_sourse)
print(file=file_sourse)
print('',f' Ваше имя - {name}, Ваша фамилия - {surname} ', end='! >>>>', sep='<<<< ? ', file=file_sourse)

file_sourse.close()

