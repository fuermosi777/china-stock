import unittest
from china_stock import Stock

class TestStock(unittest.TestCase):

    def setUp(self):
        sample = ['sh000001', 'sh000002', 'sh601006']
        self.stock = Stock(sample)

    def test_dict(self):
        data = self.stock.get_data()
        self.assertEqual(len(data[0]), 10)

if __name__ == '__main__':
    unittest.main()