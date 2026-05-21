SUPPORTED_LANGUAGES = [
    "Hindi",
    "English",
    "Gujarati",
    "Marathi",
    "Tamil",
    "Telugu",
    "Kannada",
    "Bengali",
    "Punjabi",
    "Malayalam"
]


def get_supported_languages():
    return {
        "status": "success",
        "languages": SUPPORTED_LANGUAGES
    }


def set_language(language):
    if language not in SUPPORTED_LANGUAGES:
        return {
            "status": "error",
            "message": "Language not supported"
        }

    return {
        "status": "success",
        "selected_language": language,
        "message": f"{language} language selected"
    }