"use strict";

function loadChartDemo() {
  const chartBox = document.getElementById("chartBox");
  if (!chartBox) return;

  chartBox.innerHTML = `
    <div>
      <h3>📊 Analytics Chart Ready</h3>
      <p>Backend data connect hone ke baad live chart dikhega.</p>
    </div>
  `;
}

function updateChartText(text) {
  const chartBox = document.getElementById("chartBox");
  if (chartBox) chartBox.textContent = text;
}