try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import chinastock.stock.service as cs_service
import json
from datetime import datetime

GET_STOCK_TODAY_URL = 'http://img1.money.126.net/data/hs/time/today/%s%s.json'

def get_stock_today(code, exchange):
	exchange = cs_service.exchange_to_num(exchange)
	response = urlopen(GET_STOCK_TODAY_URL%(exchange, code))
	data = json.loads(response.read())
	price = data['data']
	date = data['date']
	res = [[datetime.strptime(date + d[0], '%Y%m%d%H%M'), d[1], d[3]] for d in price]
	return res