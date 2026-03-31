import yfinance as yf
from pprint import pprint

tickers = ['AAPL', 'NVDA', "MSFT", "GOOG" "META"]
stocks = {}

for t in tickers: 
    stocks[t] = yf.Ticker(t).info[ 'currentPrice']
    # create a dictionary with the current price of each stock

    print(stocks)

    print('After sorting...')

    def sort_by_price(t):
        return t[1] # sort by the second item in the tuple, which is the price
    
    # print(sorted(stocks.items(), key=sort_by_price))
    print(sorted(stocks.items(), key=lambda t: t[1])) # same as above but using a lambda function instead of defining a separate function
    