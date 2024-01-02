import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from helpers import apology, login_required, lookup, usd

# export API_KEY=pk_c1a75a8adfe444199e315ddce061c56f

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get user ID
    user_id = session["user_id"]

    # Get variables for the columns' data from the transactions database
    columns = db.execute("SELECT symbol, name, SUM(shares) AS shares, cost FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)

    # Get the users remaining cash
    cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_db[0]["cash"]

    return render_template("portfolio.html", columns=columns, cash=cash)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    else:

        # Get variables
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Check user input is valid
        if not symbol:
            return apology("Symbol not given")
        if shares < 1:
            return apology("Shares not given")

        # Lookup stock
        stock = lookup(symbol)

        # Calculate the cost of purchase
        purchase_cost = stock["price"] * shares

        # Store how much cash the user has available into a variable we can work with
        user_id = session["user_id"]
        user_cash_available = db.execute("SELECT cash FROM users WHERE id = :id", id = user_id)
        user_cash = user_cash_available[0]["cash"]

        # Check to see if the user has enough cash to make the purchase
        if purchase_cost > user_cash:
            return apology(f"Insufficient funds to make purchase. You have {user_cash}. You need {purchase_cost} for this purchase.")

        # Update the users cash remaining
        new_user_cash = user_cash - purchase_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_user_cash, user_id)

        # Store transaction data into table
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, cost, date, name) VALUES(?, ?, ?, ?, ?, ?)", user_id, stock["symbol"], shares, purchase_cost, date, stock["name"])

        # Add flash message
        flash("Purchase successful!")

        # Redirect to portfolio
        return redirect("/")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT * FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions_db)

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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    else:

        # Get variables
        symbol = request.form.get("symbol")

        # Check for valid user input
        if not symbol:
            return apology("Please provide a symbol")

        # Lookup symbol information
        stock = lookup(symbol.upper())

        # Check stock is valid
        if stock == None:
            return apology("Symbol does not exists")

        # Render the page with quoted information
        return render_template("quoted.html", name=stock["name"], price=stock["price"], symbol=stock["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    else:

        # Get variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Render apology for invalid entries
        if not username:
            return apology("Username not given")
        if not password:
            return apology("Password not given")
        if not confirmation:
            return apology("Password was not confirmed")
        if confirmation != password:
            return apology("Password and confirmation does not match")

        # Create a hash of the password
        hash = generate_password_hash(password)

        # Add login details to database
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        except:
            return apology("Username already taken")

        # Create a session for the user so they can skip login
        session["user_id"] = new_user

        # Redirect to portfolio page
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":

        # Get list of symbols in user portfolio
        user_id = session["user_id"]
        symbols_db = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", user_id)

        # Render the page
        return render_template("sell.html", symbols=[row["symbol"] for row in symbols_db])

    else:
        # Get variables
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Check user input is valid
        if not symbol:
            return apology("Symbol not given")
        if shares < 1:
            return apology("Shares not given")

        # Make sure user has enough shares to sell
        user_id = session["user_id"]
        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)
        user_shares_real = user_shares[0]["shares"]
        if shares > user_shares_real:
            return apology("Insufficient shares available to sell")


        # Lookup stock
        stock = lookup(symbol)

        # Calculate the cost of purchase
        purchase_cost = stock["price"] * shares

        # Store how much cash the user has available into a variable we can work with
        user_cash_available = db.execute("SELECT cash FROM users WHERE id = :id", id = user_id)
        user_cash = user_cash_available[0]["cash"]

        # Update the users cash remaining
        new_user_cash = user_cash + purchase_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_user_cash, user_id)

        # Store transaction data into table
        date = datetime.datetime.now()
        db.execute("INSERT INTO transactions (user_id, symbol, shares, cost, date, name) VALUES(?, ?, ?, ?, ?, ?)", user_id, stock["symbol"], (-1) * shares, purchase_cost, date, stock["name"])

        # Add flash message
        flash("Sold successfully!")

        # Redirect to portfolio
        return redirect("/")