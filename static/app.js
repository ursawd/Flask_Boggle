"use strict";
//  capture guessed word by listening for button click
$("#submit-guess").on("click", (e) => {
  e.preventDefault();
  handleGuess();
});
function handleGuess() {
  //   retrieve guessed word from input element
  let guess = $("#word-guess").val();
  $("#word-guess").val(""); //reset guess input element to blank
}
