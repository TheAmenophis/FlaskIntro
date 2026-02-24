from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/coinflip")
def coinflip():
    return render_template("coinflip.html")

@app.route("/coindata")
def coindata():
    print(request.args["vrednost"])
    rnd = random.randint(0,1)
    status = ["HEADS", "TAILS"][rnd]
    if rnd==0:
        return {"img" : "https://i.postimg.cc/CBNJNfDJ/head.png", "status" : status}
    else:
        return {"img" : "https://i.postimg.cc/zysdXN8w/tail.png", "status" : status}

app.run(debug=True)