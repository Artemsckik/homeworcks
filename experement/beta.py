import openpyxl
from datetime import datetime
file_path = r'C:\Users\stari\Desktop\homeworcks\ final project\Таблица ЕКСЕЛЬ.xlsx'
info = 'Jhon Macklein B 10.2.1900 10.3.1980'
book = openpyxl.open(fr'{file_path}')
sheet = book.active
info = info.split()
if len(info) == 5:
    info = [f'{info[0]} {info[1]} {info[2]}',f'{info[3]}',f'{info[4]}']
    row = sheet.max_row + 1
    sheet[row][0].value = info[0]
    sheet[row][1].value = info[1]
    sheet[row][2].value = info[2]
elif len(info) > 6:
    print('Много')
else:
    print('мало')
