"""Boogle Game - Unit 19-5"""
from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-phrase"

# -----------------------------------------------
"""create game board list of lists with letters"""
boggle_game = Boggle()
game_board = boggle_game.make_board()

# ----------------------------------------------
@app.route("/")
def index():
    """create game board in html page"""
    session["game_board"] = game_board
    return render_template("index.html", game_board=game_board)


@app.route("/check_word", methods=["POST"])
def check_word():
    """perform checks to see if guessed word is valid"""
    # get word to check from request that was passed
    # into route by js axios call
    word = request.json["word"]
    # check if incoming word in word list or on board
    """ returns ok, not-on-board, not-word"""
    status = boggle_game.check_valid_word(game_board, word)
    check_result_json = jsonify(result=status)
    return check_result_json
