import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime,date

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")
db = SQL(os.getenv("DATABASE_UR"))


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
    current_price={}
    response={}
    total={}
    query= db.execute("SELECT userid,symbol,name,quantity FROM holdings WHERE userid=:userid ",userid=session["user_id"])
    cashq= db.execute("SELECT cash FROM users WHERE id=:userid",userid=session["user_id"])
    gtotal=cashq[0]["cash"]
    for j in query:
        total[j["symbol"]] = lookup(j["symbol"])["price"] * int(j["quantity"])
        current_price[j["symbol"]]=lookup(j["symbol"])["price"]
        gtotal=gtotal+total[j["symbol"]]

    return render_template("index.html",gtotal=gtotal,query=query,cash=cashq[0]["cash"],total=total,current_price=current_price)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html")
    else:
        capital= db.execute("SELECT cash FROM users WHERE id=:userid",userid=session["user_id"])
        if request.form.get("symbol") == None:
            return apology("Symbol required")

        elif request.form.get("shares") == None:
            return apology("Invalid quantity")

        elif lookup(request.form.get("symbol")) == None:
            return apology("Invalid symbol")

        elif capital[0]["cash"] < lookup(request.form.get("symbol"))["price"] * int(request.form.get("shares")):
            return apology("Insufficient funds")

        else:
            today = date.today()
            d = today.strftime("%d/%m/%Y")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            response=lookup(request.form.get("symbol"))
            amount= response["price"] * int(request.form.get("shares"))
            response=lookup(request.form.get("symbol"))
            trade= db.execute("INSERT INTO transactions (userid,date,time,symbol,name,price,quantity,total) VALUES (:userid,:date,:time,:symbol,:name,:price,:quantity,:total)",userid=session["user_id"],date=d,time=current_time,symbol=request.form.get("symbol"), name=response["name"], price=response["price"],quantity=request.form.get("shares"),total=amount )
            update= db.execute("UPDATE users SET cash=:amt WHERE id=:userid ", amt=capital[0]["cash"]-amount,userid=session["user_id"])
            check=db.execute("SELECT symbol FROM holdings WHERE symbol=:symbol AND userid=:userid",symbol=request.form.get("symbol"),userid=session["user_id"])
            if len(check) < 1:
                update_holdings=db.execute("INSERT INTO holdings (userid,symbol,name,quantity) VALUES (:userid,:symbol,:name,:quantity)", userid=session["user_id"], symbol=request.form.get("symbol"),name=lookup(request.form.get("symbol"))["name"],quantity=request.form.get("shares"))
            else:
                quant=db.execute("SELECT quantity FROM holdings WHERE userid=:userid AND symbol=:symbol ",userid=session["user_id"], symbol=request.form.get("symbol"))
                update_holdings=db.execute("UPDATE holdings SET quantity=:q WHERE symbol=:symbol AND userid=:userid",q=int(quant[0]["quantity"])+int(request.form.get("shares")), symbol=request.form.get("symbol"),userid=session["user_id"])
            flash('Bought!')
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])

    return render_template("history.html", transactions=transactions)

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
    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
