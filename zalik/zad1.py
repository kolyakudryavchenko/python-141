'''
Кудрявченко Микола, 141
Для всіх
1.Запитати у користувача код регіону
2.Отримати ЗВО з вказаного користувачем регіону
3.Зберегти всі дані у файл universities.csv у форматі csv
4.Збережіть ті ж дані у файл universities_<код регіону>.csv, наприклад universities_80.csv
5.Якщо регіон не зі списку доступних, то повідомити про це користувачеві у консолі
'''

import openpyxl
from openpyxl import load_workbook
import requests
import csv
print("Коди регіонів: 01	Автономна Республіка Крим"
'05	Вінницька область'
'07	Волинська область'
'12	Дніпропетровська область'
'14	Донецька область'
'18	Житомирська область'
'21	Закарпатська область'
'23	Запорізька область'
'26	Івано-Франківська область'
'32	Київська область'
'35	Кіровоградська область'
'44	Луганська область'
'46	Львівська область'
'48	Миколаївська область'
'51	Одеська область'
'53	Полтавська область'
'56	Рівненська область'
'59	Сумська область'
'61	Тернопільська область'
'63	Харківська область'
'65	Херсонська область'
'68	Хмельницька область'
'71	Черкаська область'
'73	Чернівецька область'
'74	Чернігівська область'
'80	КИЇВ'
'85	м.Севастополь')
print('введіть код регіону:')
n=str(input())
a=load_workbook('regions.xlsx')
p=a['Аркуш1']
st=p['A']
code_index=[]

for i in range(len(st)):
    cod=st[i].value
    code_index.append(cod)
code_index.pop(0)

if n in code_index:
    r=requests.get(f'https://registry.edbo.gov.ua/api/universities/?ut=1&lc={n}&exp=json')
    universities: list=r.json()

    with open('universities.csv', mode='w', encoding='cp1251', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)

    with open(f'universities_{n}.csv', mode='w', encoding='cp1251', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=universities[0].keys())
        writer.writeheader()
        writer.writerows(universities)
    print(f"Данні записані у файли universities.csv и universities_{n}.csv!")
else:
    print("Помилка: такого регіона не існіє")

