from china_stock.chinastock import Query

class Stock():

    def __init__(self, ticker):
        self.ticker = ticker
        q = Query(self.ticker)
        q.request_data()
        q.process_data()
        self.data = q.get_data()

    def get_data(self):
        return self.data