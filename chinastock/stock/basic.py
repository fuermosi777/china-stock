import chinastock.stock.service as service
from chinastock.source import netease
import json
from datetime import datetime

def get_stock_today(code, exchange):
    exchange = service.exchange_to_num(exchange)
    url = netease.STOCK_TODAY%(exchange, code)
    data = service.get_json(url)
    price = data['data']
    date = data['date']
    res = [[date + d[0], d[1], d[3]] for d in price]
    return res

def get_stock_history(code, exchange):
    exchange = service.exchange_to_num(exchange)
    url = netease.STOCK_HISTORY%(exchange, code)
    data = service.get_json(url)
    times = data['times']
    closes = data['closes']
    res = [[t, c] for (t, c) in zip(times, closes)]
    return res

def get_stock_history_adj(code, exchange, year=None):
    if not year:
        year = datetime.now().year 
    exchange = service.exchange_to_num(exchange)
    url = netease.STOCK_HISTORY_ADJ%(year, exchange, code)
    data = service.get_json(url)
    prices = data['data']
    res = prices
    return res