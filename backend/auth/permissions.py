PERMISSIONS = {
    "owner": [
        "dashboard",
        "products",
        "stock",
        "billing",
        "khata",
        "payments",
        "reports",
        "whatsapp",
        "ai",
        "settings"
    ],
    "staff": [
        "dashboard",
        "billing",
        "stock_view",
        "expense_entry"
    ]
}


def has_permission(role, permission):
    return permission in PERMISSIONS.get(role, [])