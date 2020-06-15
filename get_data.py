import pandas_datareader.data as web
import datetime
import pandas as pd

# Gets the data from Yahoo Finance
def get_stock_data(stock_ticker) :
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    data_price_list = web.DataReader(stock_ticker, 'yahoo', start_date, end_date)
    return data_price_list

def open_portfolio():
    data = pd.read_csv('MyPortfolio\MyStocks.csv') # To run for other files
    # data = pd.read_csv('MyStocks.csv') To run the program alone
    # Ticker,Shares,Purchase_Price
    return data

if __name__ == '__main__':
    open_portfolio()