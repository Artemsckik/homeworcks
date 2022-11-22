# Прочитать сохранённый json-файл из задания №17 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import json
import csv


with open('sources.json') as source:
    sources = json.load(source)
    name_of_filed = ['Имя', 'Возраст']
    user_age = [sources[x] for x in sources]
with open('sources.csv', 'w', encoding='utf-8') as s:
    file_writer = csv.writer(s)
    for item in (name_of_filed, *user_age):
        file_writer.writerow(item)





