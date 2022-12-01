import csv
from openpyxl import  load_workbook

with open(r'C:\Users\stari\Desktop\homeworcks\ final project\sources.csv', encoding='utf-8') as s:
    file_reader = csv.reader(s)
    sourse = list(file_reader)

fn = r'C:\Users\stari\Desktop\homeworcks\ final project\Таблица ЕКСЕЛЬ.xlsx'
wb = load_workbook(fn)
ws = wb['Sheet1']
for i in sourse:
    ws.append([i[0],i[1],i[2],i[3]])
wb.save(fn)
wb.close()
