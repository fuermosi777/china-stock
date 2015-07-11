import unittest
import chinastock as cs

class Test(unittest.TestCase):

	def set(self):
		self.code = '000001'
		self.exchange = 'SZ'

	def test_get_stock_today(self):
		self.set()
		print(cs.get_stock_today(self.code, self.exchange))