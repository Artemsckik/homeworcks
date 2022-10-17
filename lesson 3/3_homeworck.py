
user_name= input('Введите имя и фамилию ')
list_name_surname = user_name.split()

name = list_name_surname[0][::-1].upper()

surname = list_name_surname[1][::-1].capitalize()

print('',' Ваше имя - %s, Ваша фамилия - %s ' %(name,surname), end='! >>>>', sep='<<<< ? ')
print()
print('',' Ваше имя - {}, Ваша фамилия - {} '.format(name,surname) , end='! >>>>', sep='<<<< ? ')
print()
print('',f' Ваше имя - {name}, Ваша фамилия - {surname} ', end='! >>>>', sep='<<<< ? ')