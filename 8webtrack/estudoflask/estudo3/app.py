from flask import Flask, redirect, render_template, request, g
import sqlite3

DATABASE = 'froshims.db'

def getDB():
    db = getattr(g, 'database' , None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE)
    return db


SPORTS = [
"Dodgeball",
"Flag Football",
"Soccer",
"Volleyball",
"Ultimate Frisbee"
]

app = Flask(__name__)

@app.teardown_appcontext
def closeConnection(exception):
    db = getattr(g, 'database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    # Checando se o usuário preencheu corretamente o formulário em "index.html"
    if not name:
        return render_template("error.html", message="Missing name")
    # Checando se o usuário preencheu o esporte e se ele consta na nossa lista global
    sport = request.form.get("sport") # form.get para requisições do tipo "POST"
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    '''
    1. Passe a função global "getDB()" para uma variável "X" no escopo da rota.
    2. Passe a função "cursor()" como método da variável "X" anterior e coloque-a em
        uma variável "Y".
    3. Pegue essa variável "Y" e adicione a função commit() como método.   
    '''
    
    db = getDB() # Passando a função que conecta ao banco para uma variável
    c = db.cursor() # Descobrir o que a função "cursor() faz"
    c.execute("INSERT INTO registrants (name, sport) VALUES(?,?)", (name, sport))
    # Execute a query para o banco de dados
    db.commit() # Commitando no banco - descobrir o que ela faz
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row #Descobrir o row_factory faz

    c = db.cursor()
    c.execute("SELECT * FROM registrants")

    registrants = c.fetchall() #Descobrir o que Fetch faz
    
    return render_template("registrants.html", registrants=registrants)

if __name__ == '__main__':
   app.run(debug = True)