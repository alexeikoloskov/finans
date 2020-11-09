from openapi_client import openapi
from datetime import datetime
from pytz import timezone

token = 't.LXkqE4m5tEHEG370oGguujHO08FZowekQlSdHBxi6dmqNX6CNdecnE4Ow0hDASVxvq9wyoZoaJxia6NXMNeFYw'
client = openapi.api_client(token)

'1364526508:AAElJt4zNg63ViKX07ogx1fCjy3OAImiSqo'



class get_instrument():
    def price_dollar(i=14):  # i - какой доллар в портфеле
        pf = client.portfolio.portfolio_get()
        balance = pf.payload.positions[i].average_position_price.value
        WM = pf.payload.positions[i].expected_yield.value
        how_much = pf.payload.positions[i].balance
        cb = (balance * how_much) + WM
        weidth = round(cb / how_much, 3)
        return weidth

    def one(i):
        pf = client.portfolio.portfolio_get()
        print(pf)
        balance=pf.payload.positions[i].average_position_price.value
        WM=pf.payload.positions[i].expected_yield.value
        how_much = pf.payload.positions[i].balance
        b=balance*how_much
        cb=(balance*how_much)+WM
        weidth=cb/how_much
        one_percent=b/100
        how_percent=round((WM/one_percent),2)
        print('Название:', pf.payload.positions[i].name)
        print('Тикер:', pf.payload.positions[i].ticker)
        print('Валюта:', pf.payload.positions[i].average_position_price.currency)
        # if pf.payload.positions[i].average_position_price.currency == 'USD':
        #     convert =
        #     print(convert)
        print('По сколько покупал:', pf.payload.positions[i].average_position_price.value)
        print('Текущая стоимость:', weidth)
        print('Кол-во бумаг:', pf.payload.positions[i].balance)
        print('Сколько потратил:', b)
        print('Общая текущая стоимость:', cb)
        print('Сколько в +:', pf.payload.positions[i].expected_yield.value)
        print('Сколько в + в %:', how_percent)

    @staticmethod
    def all_currency():
        all_currency = client.portfolio.portfolio_currencies_get().payload.currencies
        len_currencies = int(len(all_currency))
        i = 0
        while len_currencies >= i+1:
            currency = all_currency[i]
            if currency.balance == 0.0:
                continue
            else:
                print(currency.currency,':', currency.balance)
            i+=1

    @staticmethod
    def all():
        pf = client.portfolio.portfolio_get()
        position = pf.payload.positions
        how_much = int(len(pf.payload.positions))
        k=0
        value, currency, balance, ticker, name, amount_all = [], [], [], [], [], []
        # print(how_much, ' - Общее количество инструментов')
        for i in position:
            # print('№ ', k+1)
            # print('value:', i.average_position_price.value)
            # print('currency:', i.average_position_price.currency)
            # print('balance:', i.balance)
            # print('ticker:', i.ticker)
            # print('name:', i.name)
            value.append(i.average_position_price.value)
            currency.append(i.average_position_price.currency)
            balance.append(i.balance)
            ticker.append(i.ticker)
            name.append(i.name)
            amount_all.append(i.average_position_price.value*i.balance)
            k+=1
        return value, currency, balance, ticker, name, amount_all




# Получить список опреций в портфеле
# PayIn — Пополнение брокерского счета
# PayOut — Вывод денег
# BuyCard — Покупка с карты
# Sell — Продажа
# BrokerCommission — Комиссия брокера
# Dividend — Выплата дивидендов
# Tax — Налоги
# TaxDividend- Налоги c дивидендов
# ServiceCommission — Комиссия за обслуживание
# Качаем все операции с 30 сентября 2016

class get_operation():
    def one(x,zone='Europe/Moscow'):
        d1 = datetime(2016, 9, 30, 0, 0, 0,
                      tzinfo=timezone(zone))  # timezone нужно указывать. Иначе - ошибка
        d2 = datetime.now(tz=timezone(zone))  # По настоящее время
        ops = client.operations.operations_get(_from=d1.isoformat(), to=d2.isoformat())
        # Получить инфо по одной конкретной операции
        op=ops.payload.operations[x]
        print('--------------')
        print(op.figi) # figi всегда берем из операции
        print(op.operation_type)   # и тип операции тоже
        print(op.date)
        if op.trades == None:      # Если биржевых сделок нет
            print('price:', op.price)       # Берем из операции цену бумаги
            print('payment:', op.payment)   # Сумму платежа
            print('quantity:', op.quantity) # И количество бумаг
        else:
            for t in op.trades:                   # А если есть сделки - то перебираем их
                print('price:', t.price)          # И берем данные из них
                print('quantity:', t.quantity)
                get = client.market.market_search_by_figi_get(op.figi)
                print(get.payload.name)
        print('--------------')
    def all(year,month,day=1,hour=0,minute=0,second=1,zone='Europe/Moscow'):
        # Весь список операций
        d1 = datetime(year, month, day, hour, minute, second,
                      tzinfo=timezone(zone))  # timezone нужно указывать. Иначе - ошибка
        d2 = datetime.now(tz=timezone(zone))  # По настоящее время
        ops = client.operations.operations_get(_from=d1.isoformat(), to=d2.isoformat())
        print('--------------')
        for op in ops.payload.operations: # Перебираем операции
            print(op.figi) # figi всегда берем из операции
            print(op.operation_type)   # и тип операции тоже
            print(op.date)
            if op.trades == None:      # Если биржевых сделок нет
                print('price:', op.price)       # Берем из операции цену бумаги
                print('payment:', op.payment)   # Сумму платежа
                print('quantity:', op.quantity) # И количество бумаг
            else:
                for t in op.trades:                   # А если есть сделки - то перебираем их
                    print('price:', t.price)          # И берем данные из них
                    print('quantity:', t.quantity)
                    get = client.market.market_search_by_figi_get(op.figi)
                    print(get.payload.name)
            print('--------------')
    def in_date(year=2016,month=9,day=1,year2=2016,month2=9,day2=1,zone='Europe/Moscow'):
        # Весь список операций
        d1 = datetime(year, month, day, 0, 0, 0,
                      tzinfo=timezone(zone))  # timezone нужно указывать. Иначе - ошибка
        d2 = datetime(year2, month2, day2, 0, 0, 0,
                      tzinfo=timezone(zone))  # По настоящее время
        ops = client.operations.operations_get(_from=d1.isoformat(), to=d2.isoformat())
        print('--------------')
        for op in ops.payload.operations:  # Перебираем операци
            print(op.figi)  # figi всегда берем из операции
            print(op.operation_type)  # и тип операции тоже
            print(op.date)
            if op.trades == None:  # Если биржевых сделок нет
                print('price:', op.price)  # Берем из операции цену бумаги
                print('payment:', op.payment)  # Сумму платежа
                print('quantity:', op.quantity)  # И количество бумаг
            else:
                for t in op.trades:  # А если есть сделки - то перебираем их
                    print('price:', t.price)  # И берем данные из них
                    print('quantity:', t.quantity)
                    get = client.market.market_search_by_figi_get(op.figi)
                    print(get.payload.name)
            print('--------------')

    def dividend(month,year=2020,day=1,hour=0,minute=0,second=1,zone='Europe/Moscow'):
        # Весь список операций
        d1 = datetime(year, month, day, hour, minute, second,
                      tzinfo=timezone(zone))  # timezone нужно указывать. Иначе - ошибка
        d2 = datetime.now(tz=timezone(zone))  # По настоящее время
        ops = client.operations.operations_get(_from=d1.isoformat(), to=d2.isoformat())
        print('--------------')
        for op in ops.payload.operations: # Перебираем операции
            if op.operation_type == 'Dividend':
                print(op.operation_type)
                print(op.date)
                print(op.currency,': ',op.payment)
                if op.currency == 'USD':
                    price_dollar = get_instrument.price_dollar()
                    price_in_rub = price_dollar * op.payment
                    print('В рублях: ',price_in_rub)
                name = client.market.market_search_by_figi_get(op.figi)
                print(name.payload.name)
            elif op.operation_type == 'TaxDividend':
                print(op.operation_type)
                print(op.date)
                print(op.currency, ': ', op.payment)
                name = client.market.market_search_by_figi_get(op.figi)
                print(name.payload.name)
            else:
                continue
            print('--------------')

# get_operation.dividend(10)

# get_operation.one(2)
# get_operation.all(2020, 5, 25)
# get_operation.in_date(2020,4,1,2020,4,29)
# get_instrument.one(7)
# get_instrument.all()
