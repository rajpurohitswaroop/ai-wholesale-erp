ROLES = {
    "owner": {
        "name": "Owner",
        "level": 1,
        "panel": "owner-dashboard"
    },
    "staff": {
        "name": "Staff",
        "level": 2,
        "panel": "staff-dashboard"
    }
}


def get_role(role):
    return ROLES.get(role, None)