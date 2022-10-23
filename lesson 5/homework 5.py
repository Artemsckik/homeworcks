# Ввести с клавиатуры целое число n.
#
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
#
# Реализовать в 2-х вариантах: используя цикл while и цикл for


number = int(input('Введите число: '))

q = 0

list_numbers = []

while len(list_numbers) != number:
    q += 1
    n = q * q * q
    if n % 3 == 0:
        list_numbers.append(0)
    else:
        list_numbers.append(n)
print(list_numbers)
print(sum(list_numbers))

list_numbers.clear()

q = 0

for i in range(number):
    q += 1
    n = q * q * q
    if n % 3 == 0:
        list_numbers.append(0)
    else:
        list_numbers.append(n)
print(list_numbers)
print(sum(list_numbers))
