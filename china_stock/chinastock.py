import urllib.request
import re

SOURCE = 'http://hq.sinajs.cn/list='

class Query():

    def __init__(self, tickers):
        self.tickers = tickers

    def request_data(self):
        data = urllib.request.urlopen(SOURCE + ','.join(self.tickers)).read().decode('gb2312')
        self.source_data = data

    def process_data(self):
        data_list = self.source_data.split(';\n')
        data_list.pop()
        dataset = []
        for d in data_list:
            try:
                text = re.findall(r'"(.+)"', d)[0]
                text_list = text.split(',')
                stock = {
                    'name': text_list[0],
                    'open': text_list[1],
                    'yesterday': text_list[2],
                    'price': text_list[3],
                    'high': text_list[4],
                    'low': text_list[5],    # lowest price today
                    'vol': text_list[8],    # total volume
                    'total': text_list[9],  # total amount of money of transactions
                    'date': text_list[30],
                    'time': text_list[31],
                }
                dataset.append(stock)
            except:
                print('Incorrect ticker')
                return
        self.data = dataset
        
    def get_data(self):
        return self.data