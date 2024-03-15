import yfinance as yf
import pandas as pd

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

    def list_holiday(self,period,interval):
        start_date=self.fetch_stock_data(period,interval).index.min()
        end_date=self.fetch_stock_data(period,interval).index.max()
        date_range=pd.date_range(start=start_date,end=end_date)

        index_dates=set(self.fetch_stock_data(period,interval).index)

        missing_dates=[date for date in date_range if date not in index_dates]
        return missing_dates

obj=yfinance('GOOGL')

print(obj.list_holiday('1mo','1d'))

