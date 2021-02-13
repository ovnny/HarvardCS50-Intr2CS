import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        response = requests.get(f"https://cloud-sse.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def setBuyStatus(qty, price, cash):
    qty, price, cash = int(qty), float(price), float(cash)
    tradeState = None

    totalBuy = qty * price
    tradeState = 'BUY'
    updatedCash = cash - totalBuy

    return [tradeState, totalBuy, updatedCash]


def setSellStatus(qty, price, cash, assets):
    qty, price, cash, assets = int(qty), float(price), float(cash), int(assets)
    tradeState = None
    totalSell = qty * price
    tradeState = 'SELL'
    updatedCash = cash + totalSell
    updatedAssets = assets - qty

    return [tradeState, totalSell, updatedCash, updatedAssets]

def totalPrice(qty, price):
    total = qty * price
    return total