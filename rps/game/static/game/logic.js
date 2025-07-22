let [computer_score, user_score] = [0, 0];
let result_ref = document.getElementById("result");

function checker(user_choice) {
    fetch("/play/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `user_move=${user_choice}`
    })
    .then(res => res.json())
    .then(data => {
        let computer_choice = data.computer_move;
        let winner = data.winner;

        // Update DOM
        document.getElementById("comp_choice").innerHTML = `Computer chose: <span>${computer_choice.toUpperCase()}</span>`;
        document.getElementById("user_choice").innerHTML = `You chose: <span>${user_choice.toUpperCase()}</span>`;

        if (winner === "user") {
            result_ref.innerHTML = "YOU WIN";
            result_ref.style.cssText = "background-color: blue; color: white";
            user_score++;
        } else if (winner === "computer") {
            result_ref.innerHTML = "YOU LOSE";
            result_ref.style.cssText = "background-color: red; color: white";
            computer_score++;
        } else {
            result_ref.innerHTML = "DRAW";
            result_ref.style.cssText = "background-color: yellow; color: grey";
        }

        document.getElementById("user_score").innerText = user_score;
        document.getElementById("computer_score").innerText = computer_score;
    });
}
