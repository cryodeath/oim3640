import yfinance as yf

stock = yf.Ticker ("AAPL")
info = stock.info
print(type(info))

print(info.keys())
print(len(info))
print(info['longName'])
print(info['shortName'])
print(info['currentPrice'])

# prinnt(info['longBusinessSummary'])

print(info['longBusinessSummary'].split())
print('iphone' in info['longBusinessSummary'])
# strings are case sensitive and thats why we have to use lower() to make it all lowercase and find it 

print('iPhone' in info['longBusinessSummary'])

print(info['city'])
info['city'][0] = 'c'
# doesnt work because strings are immutable, we cant change them in place, we have to create a new string if we want to change it
info['city'] = 'Wellesley'
print(info['city'])

info['founder'] = 'Robert'
print(info['founder'])

# for k, v in info.items():
#     print(k, v)

tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

print(prices)

print(sorted(prices)) # create a new list of the keys in prices, sorted alphabetically
print(sorted(prices.keys())) # same as above
print(sorted(prices.values(), reverse=True)) # create a new list of the values in prices, sorted from highest to lowest

# how to sort stocks by values, but still show k:v ?

# print(tickers)

prices = {'AAPl': 150, 'NVDA': 300, 'MSFT': 250}
print(sum(prices.values()))

total = 0 
for price in prices.values():
    total += price
print(total)

tickers.append('GOOG')
print(tickers)
# tickers = {}
for t in tickers
    prices[t] = yf.Ticker(t).info['currentPrice']
print(prices)

tickers = ['AAPL', 'NVDA', 'MSFT', 'GOOG']
stocks = {} # {'NVDA' : [open ...., currentPrice...., volume....]}

for t in tickers:
    stocks[t] = yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume'] # create a tuple of the three values and assign it to stocks[t], tuples are immutable, so we cant change them in place if we want to, but we can reassign stocks[t] to a new tuple if we want to change it

    stocks[t] = [yf.Ticker(t).info['open'], yf.Ticker(t).info['currentPrice'], yf.Ticker(t).info['volume']] # create a list of the three values and assign it to stocks[t], lists are mutable, so we can change them in place if we want to

# stocks ('AAPL')[currentPrice] = 200 # doesnt work because stocks['AAPL'] is a tuple, which is immutable, we cant change it in place, we have to create a new tuple if we want to change it
stocks['AAPL'] = ['currentPrice'] = 260
print(stocks)