import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash, safe_str_cmp

from helpers import apology, login_required, lookup, usd, setBuyStatus, setSellStatus, totalPrice
from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    # Show the user's assets on 'GET' requests(only if the stocks were bigger than 0)
    userData = db.execute("""   SELECT DISTINCT symbl, companyname, stocks
                                FROM userstatus INNER JOIN usertrade ON
                                userstatus.id=usertrade.id WHERE
                                symbl = symbol AND userstatus.id = :uid
                                AND stocks > 0""", uid=session['user_id'])
    userInfo = []
    # Sanitizing userData
    for data in userData:
        userData = list(data.values())
        userInfo.append(userData)
        
    quoted = []
    #looking for the user share's current prices
    for i in range(len(userInfo)):
        quote = lookup(userInfo[i][0])
        quote = list(quote.values())
        quoted.append(quote)

    prices = []
    # More sanitize stuff
    for quote in quoted:
        prices.append(round(quote.pop(1), 2))
    
    totalAssets = []
    for i in range(len(userInfo)):
        userInfo[i].append(prices[i])
        TOTAL = totalPrice(userInfo[i][2], userInfo[i][3])
        format(TOTAL,'.2f')
        userInfo[i].append(TOTAL)
        totalAssets.append(TOTAL)

    cash = db.execute("""   SELECT cash FROM users WHERE id = :uid""",
                            uid=session['user_id'])
    
    sumAssets = sum(totalAssets) + cash[0]['cash']

    return render_template(
        "/index.html", userInfo=userInfo, sumAssets=usd(sumAssets), cash=usd(cash[0]['cash']))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # Defining "Get" parammeters
    symbol = request.form.get("symbol")
    qty = request.form.get("quantity")

    if request.method == "POST":
        # Input Control
        if not symbol:
            return apology("Missing symbol", 403)
        elif not qty or int(qty) <= 0:
            return apology("Positive integers only", 403)

        # Consuming and sanitizing API response
        quoteShare = lookup(symbol)
        quotedShare = list(quoteShare.values())
        price = quotedShare[1]
        # Look for the user's current cash
        userState = db.execute("SELECT * from users WHERE id = :uid", uid=int(session['user_id']))
        totalCash = userState[0]['cash']

        # Checking if the user has enough cash to make the trade
        if float(totalCash) < (int(qty) * float(price)) or totalCash == None:
            return apology("You have no enough funds to purchase the assets", 404)

        # Function to set all the buy states
        updatedUserStatus = setBuyStatus(qty, price, totalCash)

        # Setting current buy's date
        today = datetime.today()
        day = today.strftime("%B %d %Y")
        hour = today.strftime("%H:%M:%S")

        # Organizing all user's information
        status= [   updatedUserStatus[0], symbol,
                    quotedShare[0], int(qty), round(price, 2),
                    round(updatedUserStatus[1], 2), day,
                    hour, session['user_id']
                ]
        # Feeding database with the purchase's information
        db.execute("""  INSERT INTO usertrade(
                        tradeState, symbol, companyname, quantity,
                        price, totaltrade, day, hour, id)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        status[0], status[1], status[2], status[3],
                        status[4], status[5], status[6], status[7], status[8], )
        # Setting new cash status
        db.execute("""  UPDATE users SET cash = ? WHERE id = id""",
                        round(updatedUserStatus[2], 2))

        lastTrade = db.execute("""  SELECT * FROM usertrade WHERE
                                    tradeState = 'BUY' AND
                                    symbol = :symbol AND id = :uid
                                    ORDER BY trade_id DESC LIMIT 1""",
                                    symbol=symbol, uid=int(session['user_id']))

        # Checking if the user already has some of the given stock
        stocks = db.execute(""" SELECT stocks FROM userstatus WHERE
                                symbl = :symbol AND
                                id = :uid""",
                                symbol=symbol,
                                uid=int(session['user_id']))
        # If not, put it in database
        if not stocks or stocks == 0:
            db.execute("""  INSERT INTO userstatus(
                            symbl, stocks, id)
                            VALUES(?, ?, ?)""",
                            lastTrade[0]['symbol'],
                            lastTrade[0]['quantity'],
                            session['user_id'])
        else:
            # Sum the new stocks with the old ones
            updatedStocks = stocks[0]['stocks'] + lastTrade[0]['quantity']
            db.execute("""  UPDATE userstatus SET
                            stocks = ? WHERE id = ?
                            AND symbl = ?""",
                            updatedStocks, session['user_id'], symbol)

        return redirect("/history")
    return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    historyTrade = db.execute("""   SELECT tradeState, symbol, quantity, price, day, hour
                                    FROM usertrade WHERE id=:uid
                                    ORDER BY day DESC, hour DESC""",
                                    uid=int(session['user_id']))
    list(historyTrade[0].values())

    return render_template("/history.html", historyTrade=historyTrade)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    # Getting input
    symbol = request.form.get("symbol")
    # Input Control
    if request.method == "POST":
        if not symbol:
            return apology("Missing symbol", 404)
        # Consuming API
        quote = lookup(symbol)

        return render_template("/quoted.html", quote=quote)
    return render_template("/quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    # Getting input via "Get"
    email = request.form.get("email")
    password = request.form.get("password")
    confirmPassword = request.form.get("confirmPassword")
    # Input control
    if request.method == "POST":
        if not email:
            return apology("Missing email", 403)
        elif not password:
            return apology("Missing password", 403)
        # Compare if the passwords match with each other
        elif safe_str_cmp(password, confirmPassword) == False:
            return apology("Unmatching passwords", 403)
        # Checking if the user already exists
        userName = db.execute("SELECT username FROM users WHERE username = ?", email)
        if not userName or userName == None:
            # Encripting the password and salve it with the username in the database
            createPassword = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users(username, hash) VALUES(?, ?)",
                        email, createPassword)

        return redirect("/login")
    return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # look for the user's assets and show it on a list in '/sell.html' via 'GET'
    userShares = db.execute(""" SELECT DISTINCT symbl
                                FROM userstatus
                                WHERE id = :uid AND stocks > 0""",
                                uid=int(session['user_id']))

    # Getting data from sell's form via 'POST'
    if request.method == 'POST':
        qty = request.form.get("quantity")
        share = request.form.getlist("userShares")
        symbol = share[0]

        # Control/validate the user's inputs
        if not qty or int(qty) < 1:
            return apology("Missing quantity", 403)
        if not symbol:
            return apology("Missing share's symbol", 403)

        # Getting quote from API
        quoteShare = lookup(symbol)

        # Sanitizing response to a list of values
        quotedShare = list(quoteShare.values())
        price = quotedShare[1]

        # Getting user status - total cash
        userState = db.execute("SELECT * FROM users WHERE id = :uid", uid=int(session['user_id']))
        totalCash = userState[0]['cash']

        # Getting user status - assets to sell, etc
        assets = db.execute(""" SELECT stocks FROM userstatus WHERE
                                symbl = :symbol AND
                                id = :uid""", symbol=symbol,
                                uid=session['user_id'])

        # Processing Sell
        if int(assets[0]['stocks']) < int(qty):
            return apology("You don't have enought stocks to make this trade", 404)
        elif not assets or int(assets[0]['stocks']) < 1 or assets == None:
            return apology("Must be a positive integer", 403)

        updatedUserStatus = setSellStatus(  qty, price,
                                            totalCash,
                                            assets[0]['stocks'])
        # Getting sell's date and time
        today = datetime.today()
        day = today.strftime("%B %d %Y")
        hour = today.strftime("%H:%M:%S")

        # Updated Status
        status= [   updatedUserStatus[0], symbol,
                    quotedShare[0], int(qty), round(price, 2),
                    round(updatedUserStatus[1], 2), day,
                    hour, session['user_id']
                ]
        # Update database(usertrade) with new trade data
        db.execute("""  INSERT INTO usertrade(
                        tradeState, symbol, companyname,
                        quantity, price, totaltrade, day, hour, id)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        status[0], status[1], status[2], status[3], status[4],
                        status[5], status[6], status[7], status[8])

        # Update the database(users) with new cash status
        db.execute("""  UPDATE users SET cash = ? WHERE id = id""",
                        round(updatedUserStatus[2], 2))

        # Update the database with new stocks status
        db.execute("""  UPDATE userstatus SET
                        stocks = ? WHERE
                        symbl = ? AND id = ?""",
                        updatedUserStatus[3],
                        symbol, session['user_id'])

        return redirect("/history")
    return render_template("/sell.html", userShares=userShares)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)