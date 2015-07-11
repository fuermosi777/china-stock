def exchange_to_num(exchange_str):
	if exchange_str == 'SS':
		return 0
	elif exchange_str == 'SZ':
		return 1
	else:
		raise NameError('Exchange name is not correct')