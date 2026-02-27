async function askAI() {
  const input = document.getElementById("userInput").value;
  const res = await fetch("/api/assistant", {
    method: "POST",
    body: JSON.stringify({ question: input })
  });
  const data = await res.json();

  document.getElementById("chatBox").innerHTML +=
    "<p><b>You:</b> " + input + "</p>" +
    "<p><b>NTG-Z:</b> " + data.response + "</p>";

  localStorage.setItem("questions",
    (Number(localStorage.getItem("questions")) || 0) + 1);
}

async function generateNotes() {
  const text = document.getElementById("noteInput").value;
  const res = await fetch("/api/notes", {
    method: "POST",
    body: JSON.stringify({ text: text })
  });
  const data = await res.json();
  document.getElementById("noteOutput").innerHTML =
    "<h3>Summary</h3>" + data.summary +
    "<h3>Key Points</h3>" + data.key_points.join("<br>") +
    "<h3>Practice Questions</h3>" + data.questions.join("<br>");
}

function startTimer() {
  let time = 1500;
  const timer = setInterval(() => {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;
    document.getElementById("timer").innerText =
      minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
    time--;
    if (time < 0) {
      clearInterval(timer);
      localStorage.setItem("sessions",
        (Number(localStorage.getItem("sessions")) || 0) + 1);
    }
  }, 1000);
}
