"use strict";

function getAISuggestion(type = "stock") {
  const suggestions = {
    stock: "Sugar stock low ho raha hai. Reorder karna better rahega.",
    payment: "3 customers ke payment due hain. Reminder bhejna chahiye.",
    sales: "Oil aur Sugar fast-selling products hain."
  };

  return suggestions[type] || "AI suggestion ready.";
}

function showAISuggestion(type = "stock") {
  const box = document.getElementById("aiSuggestion");
  if (box) {
    box.textContent = getAISuggestion(type);
  }
}