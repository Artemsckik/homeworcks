# Созадать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений кортеж состоящий
# из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря. Записать данный словарь
# на диск в json-файл.
import json
d = {123456:("Bob", 13),123056:("Bob", 13),128456:("Bob", 13),127456:("Bob", 13),122456:("Bob", 13),123486:("Bob", 13)}

with open('sources.json', 'w') as source:
    json.dump(d, source)