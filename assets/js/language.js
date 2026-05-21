"use strict";

const translations = {
  en: {
    dashboard: "Dashboard",
    billing: "Billing",
    products: "Products",
    reports: "Reports",
    settings: "Settings"
  },
  hi: {
    dashboard: "डैशबोर्ड",
    billing: "बिलिंग",
    products: "प्रोडक्ट्स",
    reports: "रिपोर्ट्स",
    settings: "सेटिंग्स"
  },
  gu: {
    dashboard: "ડેશબોર્ડ",
    billing: "બિલિંગ",
    products: "પ્રોડક્ટ્સ",
    reports: "રિપોર્ટ્સ",
    settings: "સેટિંગ્સ"
  }
};

function changeLanguage(lang) {
  localStorage.setItem("language", lang);
  applyLanguage();
}

function applyLanguage() {
  const lang = localStorage.getItem("language") || "en";
  const selected = translations[lang] || translations.en;

  document.querySelectorAll("[data-lang]").forEach((item) => {
    const key = item.getAttribute("data-lang");
    if (selected[key]) {
      item.textContent = selected[key];
    }
  });
}