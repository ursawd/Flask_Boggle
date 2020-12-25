"use strict";
let score = 0;
//  capture guessed word by listening for button click
$("#submit-guess").on("click", (e) => {
    e.preventDefault();
    handleGuess();
});

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
function keepScore(status, guess) {
    // disreguard all status except "ok"
    if (status != "ok") {
        return;
    }
    // track / display current score
    score += guess.length; //status contains
    $("#current-score").text(score);

    return;
}
