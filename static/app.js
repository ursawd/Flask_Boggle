"use strict";
// FLASK BOGGLE GAME - FRONT END CODE
//
//^^^^^^^^^^^^^^^^^^^^^^^^^^^INITIALIZATION^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//
// running score of a single game
let score = 0;
// time remaining to continue guessing
let timeRemaining = 15;

let highScore = 0;
let gamesPlayed = 0;
//
//^^^^^^^^^^^^^^^^^^^^^^^^^^GAME OPERATION^^^^^^^^^^^^^^^^^^^^^^^^^^^
//
// create / display seconds to go in game
// stop after 60 seconds
let kill = setInterval(() => {
    timeRemaining -= 1;
    $("#time-remaining").text(timeRemaining);
    if (timeRemaining == 0) {
        clearInterval(kill);
        $("#guess").text("GAME OVER");
        displayStats();
    }
}, 1000);

//^^^^^^^^^^^^^^^^^^^^^EVENT LISTENERS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//
//  capture guessed word by listening for button click
$("#submit-guess").on("click", (e) => {
    e.preventDefault();
    handleGuess();
});

//^^^^^^^^^^^^^^^^^^^^^^FUNCTIONS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//
async function handleGuess() {
    //   retrieve guessed word from input element
    let guess = $("#word-guess").val();
    $("#word-guess").val(""); //reset guess input element to blank

    // send guessed word to server to check if valid
    // response contains what is sent back by server
    let prams = {
        word: guess,
        test: "test",
    };
    let response = await axios.post("/check_word", prams);
    $("#checked").text("Guess status: " + response.data["result"]);
    keepScore(response.data["result"], guess);
}
//------------------------------------------------------------------
function keepScore(status, guess) {
    // keeps / displays current game score
    //
    // disreguard all status except "ok"
    if (status != "ok") {
        return;
    }
    // track / display current score
    score += guess.length; //status contains
    console.log(score, highScore);
    if (score > highScore) {
        highScore = score;
        $("#high-score").text(highScore);
    }
    $("#current-score").text(score);
    return;
}
//------------------------------------------------------------------
async function displayStats() {
    //pass highscore to server, get games played in return
    // update games played on board
    let prams = {
        highscore: highScore,
    };
    let response = await axios.post("/scores", prams);
    console.log(response);

    gamesPlayed = response.data["gamesplayed"];

    $("#games-played").text(gamesPlayed);
}
