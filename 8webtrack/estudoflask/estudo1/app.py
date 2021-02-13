from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("saudacao.html", name=request.form.get("name", "world"))




'''
@app.route("/saudacao", methods=["POST"])
def saudacao():
    return render_template("saudacao.html", name=request.form.get("name", "world"))
'''