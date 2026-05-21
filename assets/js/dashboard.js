"use strict";

function protectDashboard() {
  const role = localStorage.getItem("userRole");

  if (!role) {
    window.location.href = "../auth/owner-login.html";
  }
}

function logout() {
  localStorage.removeItem("userRole");
  window.location.href = "../auth/owner-login.html";
}

function setDashboardRoleText() {
  const roleText = document.getElementById("roleText");
  const role = localStorage.getItem("userRole");

  if (roleText) {
    roleText.textContent = role ? role.toUpperCase() : "GUEST";
  }
}

function loadDashboard() {
  protectDashboard();
  setDashboardRoleText();
}