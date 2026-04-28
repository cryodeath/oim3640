from flask import Flask, render_template, request
from stocks import get_stock_overview

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hello.html", name="World")


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name is None:
        name = "World"
    name = name.capitalize()
    return render_template("hello.html", name=name)


@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    # return f'The square of {number} is {number ** 2}'
    return render_template('square.html', number=number, square=result)


#create another route that shows the current price of any stocks or temperature of any city
# /weather/<city>
# /stock/<ticker>

@app.route('/stock/<ticker>')
def stock(ticker):
    ticker_value = ticker.strip()
    price = None
    last_hour = None
    day = None
    rating = None
    error = None

    try:
        stock_data = get_stock_overview(ticker_value)
        price = stock_data['price']
        last_hour = stock_data['last_hour']
        day = stock_data['day']
        rating = stock_data['rating']
        ticker_value = stock_data['ticker']
    except Exception:
        error = f"Ticker '{ticker_value.upper()}' is invalid. Please try again."

    return render_template('stock.html', ticker=ticker_value.upper(), price=price, last_hour=last_hour, day=day, rating=rating, error=error)

@app.route('/ticker', methods=['GET', 'POST'])
def ticker():
    ticker_value = ''
    price = None
    last_hour = None
    day = None
    rating = None
    error = None

    if request.method == 'POST':
        ticker_value = request.form.get('ticker', '').strip()
        if ticker_value:
            try:
                stock_data = get_stock_overview(ticker_value)
                price = stock_data['price']
                last_hour = stock_data['last_hour']
                day = stock_data['day']
                rating = stock_data['rating']
                ticker_value = stock_data['ticker']
            except Exception:
                error = f"Ticker '{ticker_value.upper()}' is invalid. Please try again."
        else:
            error = 'Please enter a ticker symbol.'

    return render_template('stock.html', ticker=ticker_value.upper() if ticker_value else None, price=price, last_hour=last_hour, day=day, rating=rating, error=error)

if __name__ == "__main__":
    app.run(debug=True)