
import ccxt
import json

name_exchanges = ["binance", "bybit"]
symbol = 'BTC/USDT'

exchanges = {}
for id in name_exchanges:
    #getattr возврашает значение атрибута по имени этого атрибута. 
    #Т.Е. Вернет обект ccxt с атрибутом binance - ccxt.binance
    exchange = getattr(ccxt, id)
    #Данной строкой записываем в словарь exchanges id {"binance": ccxt.binance} ну и так по всем name_exchanges
    exchanges[id] = exchange()
print (exchanges)
data = {}
for id, exchange in exchanges.items():
    ticker = exchange.fetch_ticker(symbol)
    data[id] = ticker['last']
print(data)

data_all = {}
for id, exchange in exchanges.items():
    markets = exchange.load_markets()
    for symbol in markets:
        ticker = exchange.fetch_ticker(symbol)
        if 'last' in ticker:
            if symbol not in data_all:
                data_all[symbol] = {}
            data_all[symbol][id] = ticker['last']


with open('btc_usdt_courses_all.json', 'w') as json_file:
    json.dump(data_all, json_file, indent=4)
print ("Готово")