from flask import Flask, render_template, request
from stocks import get_price

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
    error = None
    price = None
    try:
        price = get_price(ticker)
        if price is None:
            raise ValueError('Invalid ticker')
    except Exception:
        error = f"Ticker '{ticker.upper()}' is invalid. Please try again."
    return render_template('stock.html', ticker=ticker.upper(), price=price, error=error)

@app.route('/ticker', methods=['GET', 'POST'])
def ticker():
    ticker = ''
    price = None
    error = None

    if request.method == 'POST':
        ticker = request.form.get('ticker', '').strip()
        if ticker:
            try:
                price = get_price(ticker)
                if price is None:
                    raise ValueError('Invalid ticker')
            except Exception:
                error = f"Ticker '{ticker.upper()}' is invalid. Please try again."
        else:
            error = 'Please enter a ticker symbol.'

    return render_template('stock.html', ticker=ticker.upper() if ticker else None, price=price, error=error)

if __name__ == "__main__":
    app.run(debug=True)