"use strict";

const ERP = {
  appName: "AI Wholesale ERP",
  version: "1.0.0",

  goTo(path) {
    window.location.href = path;
  },

  showToast(message) {
    alert(message);
  },

  getRole() {
    return localStorage.getItem("userRole");
  }
};

console.log(`${ERP.appName} loaded`);