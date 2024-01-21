from flask import Flask, render_template, request, redirect

SPORTS = [
    "Tennis",
    "Soccer",
    "Rugby"
]

REGISTRANTS = {}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    # Check submission is valid
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or not sport in SPORTS:
        return render_template("failure.html")

    # Add data to dictionary
    REGISTRANTS[name] = sport

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)