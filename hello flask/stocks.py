import yfinance as yf


def _summarize_history(df):
    if df.empty:
        return None

    open_price = float(df['Open'].iloc[0])
    close_price = float(df['Close'].iloc[-1])
    high_price = float(df['High'].max())
    low_price = float(df['Low'].min())
    change = close_price - open_price
    percent = (change / open_price * 100) if open_price else 0.0

    return {
        'open': open_price,
        'close': close_price,
        'high': high_price,
        'low': low_price,
        'change': change,
        'percent': percent,
    }


def get_price(ticker):
    return get_stock_overview(ticker)['price']


def get_stock_overview(ticker):
    if not ticker or not ticker.strip():
        raise ValueError('Ticker symbol is required')

    ticker_symbol = ticker.strip().upper()
    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
    if price is None:
        raise ValueError('Invalid ticker')

    history_data = stock.history(period='1d', interval='1m')
    if history_data.empty:
        history_data = stock.history(period='5d', interval='15m')

    last_hour = None
    day = None
    if not history_data.empty:
        last_hour = _summarize_history(history_data.tail(60))
        day = _summarize_history(history_data)

    rating = {
        'recommendation': (info.get('recommendationKey') or 'N/A').capitalize(),
        'mean': info.get('recommendationMean'),
        'analyst_opinions': info.get('numberOfAnalystOpinions'),
        'trend': info.get('recommendationTrend') or []
    }

    return {
        'ticker': ticker_symbol,
        'price': price,
        'last_hour': last_hour,
        'day': day,
        'rating': rating,
    }


if __name__ == "__main__":
    print(get_stock_overview("AAPL"))
