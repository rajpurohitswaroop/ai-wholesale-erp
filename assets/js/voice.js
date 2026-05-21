"use strict";

function startVoiceOrder() {
  alert("Voice AI demo started. Real speech-to-text backend se connect hoga.");
}

function previewVoiceOrder(text) {
  const box = document.getElementById("voicePreview");

  if (box) {
    box.textContent = text || "Preview: 10 bag sugar, 5 oil tin";
  }
}

function confirmVoiceOrder() {
  alert("Order confirmed. Ab final bill generate hoga.");
}

function editVoiceOrder() {
  alert("Please corrected order dobara send karein.");
}