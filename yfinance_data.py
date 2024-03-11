import yfinance as yf

class yfinance:

    def __init__(self,stock_name):
        self.ticker=yf.Ticker(stock_name)

    def get_stock_info(self):
        return self.ticker.info
    
    def fetch_stock_data(self,period,interval):
        return self.ticker.history(period=period,interval=interval)
    
    def get_stock_earning_date(self):
        return [date.strftime('%d-%m-%Y') for date in self.ticker.earnings_dates.index]
    
        
    def get_stock_news(self):
        news=self.ticker.news
    
obj=yfinance('GOOGL')


print(obj.get_stock_earning_date())