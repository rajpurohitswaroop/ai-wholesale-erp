"use strict";

function sendWhatsAppMessage() {
  const input = document.getElementById("chatInput");
  const messages = document.getElementById("chatMessages");

  if (!input || !messages) return;

  const text = input.value.trim();
  if (!text) return;

  const customerMsg = document.createElement("div");
  customerMsg.className = "message customer-msg";
  customerMsg.textContent = text;
  messages.appendChild(customerMsg);

  const aiMsg = document.createElement("div");
  aiMsg.className = "message ai-msg";
  aiMsg.textContent = generateAIReply(text);
  messages.appendChild(aiMsg);

  input.value = "";
  messages.scrollTop = messages.scrollHeight;
}

function generateAIReply(text) {
  const lower = text.toLowerCase();

  if (lower.includes("rate") || lower.includes("price")) {
    return "AI Reply: Product rate owner dashboard se fetch hoga.";
  }

  if (lower.includes("sugar") || lower.includes("oil")) {
    return "AI Reply: Order preview ready. Please CONFIRM ya EDIT reply karein.";
  }

  if (lower.includes("pending")) {
    return "AI Reply: Aapke pending bills database se show honge.";
  }

  return "AI Reply: Message received. Kripya product name aur quantity bhejein.";
}