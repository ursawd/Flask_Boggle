"""Boogle Game - Unit 19-5"""
from flask import Flask, request, render_template, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-phrase"

boggle_game = Boggle()

# ----------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")
