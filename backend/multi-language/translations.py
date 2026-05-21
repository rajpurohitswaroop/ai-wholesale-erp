TRANSLATIONS = {
    "Hindi": {
        "dashboard": "डैशबोर्ड",
        "billing": "बिलिंग",
        "stock": "स्टॉक",
        "payment": "भुगतान"
    },
    "English": {
        "dashboard": "Dashboard",
        "billing": "Billing",
        "stock": "Stock",
        "payment": "Payment"
    },
    "Gujarati": {
        "dashboard": "ડેશબોર્ડ",
        "billing": "બિલિંગ",
        "stock": "સ્ટોક",
        "payment": "ચુકવણી"
    }
}


def translate(key, language="Hindi"):
    return TRANSLATIONS.get(language, {}).get(key, key)


def get_all_translations(language="Hindi"):
    return {
        "status": "success",
        "language": language,
        "translations": TRANSLATIONS.get(language, {})
    }