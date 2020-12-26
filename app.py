"""Boogle Game - Unit 19-5"""
from flask import Flask, request, render_template, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-phrase"

# -----------------------------------------------
"""create game board list of lists with letters"""
boggle_game = Boggle()
game_board = boggle_game.make_board()
gamesplayed = 0

# ----------------------------------------------
@app.route("/")
def index():
    """create game board in html page"""
    session["game_board"] = game_board

    if "highscore" not in session:
        session["highscore"] = 0
    if "gamesplayed" not in session:
        session["gamesplayed"] = 0

    return render_template(
        "index.html", game_board=game_board, highscore=session["highscore"], gamesplayed=session["gamesplayed"]
    )


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


@app.route("/scores", methods=["POST"])
def scores():
    """receive score / return games played
    store both in session storage"""
    # define as global variable
    global gamesplayed
    # increment games played each time route is used
    gamesplayed += 1
    # store gamesplayed in server session storage
    session["gamesplayed"] = gamesplayed

    # get game score from POST variables
    score = request.json["score"]
    highscore = session["highscore"]
    if score > highscore:
        highscore = score
    session["highscore"] = highscore

    # prepare gamesplayed value to be returned to axios call
    gamesinfo_json = jsonify(gamesplayed=gamesplayed, highscore=highscore)
    return gamesinfo_json