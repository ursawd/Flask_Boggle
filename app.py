"""Boogle Game - Unit 19-5"""
from flask import Flask, request, render_template, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-phrase"

# -----------------------------------------------
boggle_game = Boggle()
game_board = boggle_game.make_board()

# ----------------------------------------------
@app.route("/")
def index():
    session["game_board"] = game_board
    return render_template("index.html", game_board=game_board)
