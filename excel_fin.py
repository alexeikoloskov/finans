from openpyxl import load_workbook
import pandas as pd
from robot import get_instrument
from robot import get_operation


x = get_instrument.all()

value = pd.Series(x[0], name='Средняя цена покупки')
currency = pd.Series(x[1], name='Валюта')
balance = pd.Series(x[2], name='Кол-во акций')
ticker = pd.Series(x[3], name='Тикер')
name = pd.Series(x[4], name='Название')
amount_all = pd.Series(x[5], name='Стоимость ин-та в п-ле')
current_amount = pd.Series(x[6], name='Текущая стоимость ин-та')
current_amount_all = pd.Series(x[7], name='Текущая общая стоимость')

df = pd.concat([name, ticker, balance, value, amount_all, currency, current_amount, current_amount_all], axis=1)
df.round(1)
df.to_excel('example.xlsx')

col = 13
title_row = 1
k = 1

v = get_operation.dividend()
wb = load_workbook('example.xlsx')
ws = wb.active
ws.cell(column=col, row=title_row).value = 'price'
ws.cell(column=col + 1, row=title_row).value = 'date'
ws.cell(column=col + 2, row=title_row).value = 'currency'
for i in v:
    try:
        row = (x[4].index(i))+2
    except:
        row = len(x[4])+2
        k+=1
    ws.cell(column=col-1, row=row).value=i
    colomn = col
    for val in v[i]:
        if len(v[i]) == 3:
            ws.cell(column=colomn, row=row).value = val
        else:
            for d in val:
                ws.cell(column=colomn, row=row).value = d
                colomn+=1
        colomn +=1
wb.save("example.xlsx")





