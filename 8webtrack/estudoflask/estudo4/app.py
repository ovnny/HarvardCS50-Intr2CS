import os

from flask import Flask, redirect, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)


SPORTS = [
"Dodgeball",
"Flag Football",
"Soccer",
"Volleyball",
"Ultimate Frisbee"
]

#viniciusricardo.ferrera@gmail.com

@app.route("/")
def index():
    print(app.config)
    return render_template("index.html", sports=SPORTS)
    

@app.route("/register", methods=["GET", "POST"])
def register():
    email = request.form.get("email")
    # Checando se o usuário preencheu corretamente o formulário em "index.html"
    if not email:
        return render_template("error.html", message="Missing email")
    # Checando se o usuário preencheu o esporte e se ele consta na nossa lista global
    sport = request.form.get("sport") # form.get para requisições do tipo "POST"
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    

    
    return render_template("success.html")


if __name__ == '__main__':
   app.run(debug = True)