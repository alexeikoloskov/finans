import xlrd
import xlwt
from openpyxl import Workbook
from openpyxl import load_workbook
import math
import pandas as pd
from robot import get_instrument
from robot import get_operation
from pprint import pprint

x = get_instrument.all()
# print(len(x[0]))
# print(len(x[1]))
# print(len(x[2]))
# print(len(x[3]))
# print(len(x[4]))
# print(x[4])

value = pd.Series(x[0], name='Средняя цена покупки')
currency = pd.Series(x[1], name='Валюта')
balance = pd.Series(x[2], name='Кол-во акций')
ticker = pd.Series(x[3], name='Тикер')
name = pd.Series(x[4], name='Название')
amount_all = pd.Series(x[5], name='Стоимость ин-та в п-ле')
current_amount = pd.Series(x[6], name='Текущая стоимость ин-та')
current_amount_all = pd.Series(x[7], name='Текущая общая стоимость')

df = pd.concat([name, ticker, balance, value, amount_all, currency, current_amount, current_amount_all], axis=1)

pd.set_option('display.width', 500)

df.round(1)
df.to_excel('example.xlsx')

col = 12
row = 2
name_row = 1
date_col = col
price_col = col+1
currency_col = col+2
price_rub_col = col+3


v = get_operation.dividend()
pprint(v)
wb = load_workbook('example.xlsx')
ws = wb.active
for i in v:
    enter_row = 3
    ws.cell(column=col, row=name_row).value=i
    ws.cell(column=date_col, row=row).value='date'
    ws.cell(column=price_col, row=row).value='price'
    ws.cell(column=currency_col, row=row).value='currency'
    ws.cell(column=price_rub_col, row=row).value='price_rub'
    for val in v[i]:
        pprint(v[i])
        for s in val:
            pprint(val)
            for z in val[s]:
                ws.cell(column=date_col, row=enter_row).value=z[0]
                ws.cell(column=price_col, row=enter_row).value = z[1]
                ws.cell(column=currency_col, row=enter_row).value = z[2]
                try:
                    ws.cell(column=price_rub_col, row=enter_row).value = z[4]
                except:
                    ws.cell(column=price_rub_col, row=enter_row).value = ' - '
                enter_row += 1
        col+=5
wb.save("example.xlsx")





