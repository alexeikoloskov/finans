import xlrd
import xlwt
import openpyxl
import math
import pandas as pd
from robot import get_instrument

x = get_instrument.all()
# print(len(x[0]))
# print(len(x[1]))
# print(len(x[2]))
# print(len(x[3]))
# print(len(x[4]))
# print(x[4])

value = pd.Series(x[0], name='Текущая цена')
currency = pd.Series(x[1], name='Валюта')
balance = pd.Series(x[2], name='Кол-во акций')
ticker = pd.Series(x[3], name='Тикер')
name = pd.Series(x[4], name='Название')
amount_all = pd.Series(x[5], name='Стоимость ин-та в п-ле')

df = pd.concat([name, ticker, balance, value, currency, amount_all], axis=1)

df.to_excel('example.xlsx')

# df = pd.DataFrame({
# 'number': [],
# 'value': x[0],
# 'currency': x[1],
# 'balance': x[2],
# 'ticker': x[3],
# 'name': x[4]
# })
# try:
#     df.to_excel('example.xlsx')
# except:
#     print('ups...')
# file = 'fin.xlsx'
#
# my_wb = openpyxl.Workbook()
# my_sheet = my_wb.active
# b2, c2, d2, e2, f2, g2, h2 = my_sheet['B2'], my_sheet['C2'], my_sheet['D2'], my_sheet['E2'], my_sheet['F2'], \
#                              my_sheet['G2'], my_sheet['H2']
# b2.value, c2.value, d2.value, e2.value, f2.value, g2.value, h2.value  = 'Название', 'Валюта', 'Текущая стоимость', 'По сколько покупал',\
#                                                                         'Кол-во бумаг', 'Общая текущая стоимость', 'Сколько в +'
#

# c2 = my_sheet['C2']
# c2.value = 'Валюта'
# d2 = my_sheet['D2']
# d2.value = ''
# e2 = my_sheet


# my_wb.save(file)


# my_wb = openpyxl.load_workbook(file).active
#
# c1 = my_wb.cell(row=1,column=1)
# c1.value = 'хей'
#открываем файл
# rb = xlrd.open_workbook("C:\Users\79996\PycharmProjects\untitled\fin.xlsx",formatting_info=True)
# sheet = rb.sheet_by_index(0)

# wb = xlwt.Workbook()
# ws = wb.add_sheet('A Test Sheet')
#
# sg = wb.get_active_sheet(file)
# sg.write(0, 1 ,'hey')

