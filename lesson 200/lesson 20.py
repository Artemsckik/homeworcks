import os
import sqlite3

# Устанавлием соединение с БД
db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()


# Вывести все данные из таблицы employees
query_sql = '''
  SELECT *
    FROM employees;
'''

rows = cur.execute(query_sql).fetchall()

for row in rows:
    print(*row)

# Вывести CustomerId, FirstName, City, State из таблицы customers
# С возможностью фильтрации по городу и штату, которые вводит пользователь
city = input('Введите город: ')
state = input('Введите штат: ')

query_sql = '''
   SELECT CustomerId, FirstName, City, State
     FROM customers
'''

if city == '' and state == '':
    query_sql += ';'
elif city != '' and state != '':
    query_sql += f"WHERE City = '{city}' AND State = '{state}';"
elif city != '':
    query_sql += f"WHERE City = '{city}';"
elif state != '':
    query_sql += f"WHERE State = '{state}';"

print(query_sql)
print('*' * 50)

rows = cur.execute(query_sql).fetchall()

for row in rows:
    print(*row)

# Вывести уникальные FirstName из таблицы customers
# С помощью SQL
query_sql = '''
    SELECT DISTINCT FirstName
      FROM customers;
'''

# С помощью SQL + Python
query_sql = '''
    SELECT FirstName
      FROM customers;
'''

rows = cur.execute(query_sql).fetchall()
unique_first_name = set()
q = 0
for row in rows:
    unique_first_name.add(row[0])
    q += 1


print(f'all names quantity: {len(rows)}, unique names quantity: {len(unique_first_name)},{q} ')
print(*unique_first_name)

# 1) Прибыль по таблице invoice_items. Сумма по заказу = UnitPrice * Quantity (если через sql, т
# о нужно использовать sum).
# В итоге через функцию print() выводим 1 цифру общей прибыли.
# закрытие сосединения с БД

query_sql = '''
    SELECT DISTINCT UnitPrice
      FROM  invoice_items;
'''

query_sql = '''
    SELECT UnitPrice
      FROM invoice_items;
'''
rows = cur.execute(query_sql).fetchall()
UnitPrice = []
for row in rows:
    UnitPrice.append(row[0])
UnitPrice = sum(UnitPrice)

query_sql = '''
    SELECT DISTINCT UnitPrice
      FROM  invoice_items;
'''

query_sql = '''
    SELECT UnitPrice
      FROM invoice_items;
'''
Quantity = []

for row in rows:
    Quantity.append(row[0])
Quantity = sum(Quantity)
print(Quantity*UnitPrice)
connection.close()


