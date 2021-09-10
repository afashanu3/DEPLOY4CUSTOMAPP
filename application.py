from flask import Flask, request, Response
from flask import render_template
import sqlite3
import random

application = app = Flask(__name__)

@application.route("/", methods=["POST", "Get"])
def home():
    return render_template("front.html")

@application.route("/result", methods=["POST", "GET"])
def sub_budget():
    Choice = random.randint(0, 2)
    Options = ['Rock', 'Paper', 'Scissor']
    Computer = "Computer chose: " + Options[Choice]
    
    CompChoice = Options[Choice]
    if request.form.get('action') == '1':
        Player = "Rock" 
        if CompChoice == "Paper":
            WinLoseTie = "You Lose!"
        elif CompChoice == "Scissor":
            WinLoseTie = "You Win!"
        else:
            WinLoseTie = "You tied!"
    elif request.form.get('action') == '2':
        Player = "Paper" 
        if CompChoice == "Scissor":
            WinLoseTie = "You Lose!"
        elif CompChoice == "Rock":
            WinLoseTie = "You Win!"
        else:
            WinLoseTie = "You tied!"
    else:
        Player = "Scissor" 
        if CompChoice == "Paper":
            WinLoseTie = "You Win!"
        elif CompChoice == "Scissor":
            WinLoseTie = "You Tied!"
        else:
            WinLoseTie = "You Lose!"

    return render_template("front.html", choice = Computer, WinLoseTie = WinLoseTie)

app.run()
