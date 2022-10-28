
# Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.

numbers = {'Один': 1, 'Два': 2, 'Три': 3}

letter = [[numbers[a], [a]] for a in numbers]

letter = dict(letter)

print(letter)
print(numbers)