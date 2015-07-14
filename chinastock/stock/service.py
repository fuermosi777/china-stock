try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
import json

def exchange_to_num(exchange_str):
	if exchange_str == 'SS':
		return 0
	elif exchange_str == 'SZ':
		return 1
	else:
		raise NameError('Exchange name is not correct')

def get_json(url):
    try:
        response = urlopen(url)
    except:
        return None
    data = json.loads(response.read().decode())
    return data