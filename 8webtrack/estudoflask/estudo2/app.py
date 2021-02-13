from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Missing sport")
    
    REGISTRANTS[name] = sport
    
    '''
    return render_template("registrants.html", registrants=REGISTRANTS)
    OBS: UTILIZEI A FUNÇÃO "redirect" para direcionar a rota "@register" para "@registrants"
    '''

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)




'''
@app.route("/register", methods=["GET", "POST"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")
'''
