console.log('adsf')
let username =  window.location.href.substring(window.location.href.lastIndexOf("/") + 1);

fetch(`/api/risks/${username}`)
  .then(res => res.json())
  .then(risks => {
    const container = document.querySelector(".health-risks");
    container.innerHTML = ""; // vorherige Inhalte löschen

    if (risks.length === 0) {
      container.innerHTML = "<p>Es liegen aktuell keine akuten Risiken vor.</p>";
    } else {
      risks.forEach(risk => {
        const div = document.createElement("div");
        div.classList.add("risk-item");
        div.innerHTML = `
          <div class="risk-name">${risk.name}</div>
          <div class="risk-description">${risk.description}</div>
          <div class="risk-solution">
              <span class="solution-title">Solution:</span> ${risk.solution}
          </div>
        `;
        container.appendChild(div);
      });
    }
  });

function onSportClick() {
  alert("Du hast den SPORT-Kasten geklickt!");
}

function onHealthClick() {
  window.location.href = `/health/${username}`;
}

function onSleepClick() {
  alert("Du hast den SLEEP-Kasten geklickt!");
}

// Funktion für NUTRITION
function onNutritionClick() {
  alert("Du hast den NUTRITION-Kasten geklickt!");
}

// Event-Listener hinzufügen
document.getElementById('sport').addEventListener('click', onSportClick);
document.getElementById('health').addEventListener('click', onHealthClick);
document.getElementById('sleep').addEventListener('click', onSleepClick);
document.getElementById('nutrition').addEventListener('click', onNutritionClick);
