console.log("Music App Loaded");

const cards =
document.querySelectorAll(".song-card");

cards.forEach(card => {

card.addEventListener("click", () => {

console.log("Song Selected");

console.log("Music App Started");

});

});