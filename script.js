// Connect to Telegram WebApp
let tg = window.Telegram.WebApp;
tg.expand(); // Expands the app to full screen

// Function to ask a question and get AI response
function askQuestion() {
    let question = document.getElementById("question").value;

    if (question === "") {
        alert("Please enter a question!");
        return;
    }

    // API call to backend (Replace with your real backend URL)
    fetch("https://your-backend.onrender.com/ask?question=" + encodeURIComponent(question))
        .then(response => response.json())
        .then(data => {
            document.getElementById("response").innerText = "AI Mentor: " + data.answer;
        })
        .catch(error => {
            document.getElementById("response").innerText = "Error: Could not get an answer.";
            console.error("API Error:", error);
        });
}

// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("ask-btn").addEventListener("click", askQuestion);
});


