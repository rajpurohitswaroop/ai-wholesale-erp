VOICE_LANGUAGE_CODES = {
    "Hindi": "hi-IN",
    "English": "en-IN",
    "Gujarati": "gu-IN",
    "Marathi": "mr-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Kannada": "kn-IN",
    "Bengali": "bn-IN",
    "Punjabi": "pa-IN",
    "Malayalam": "ml-IN"
}


def get_voice_language_code(language="Hindi"):
    return {
        "status": "success",
        "language": language,
        "voice_code": VOICE_LANGUAGE_CODES.get(language, "hi-IN")
    }


def is_voice_language_supported(language):
    return {
        "status": "success",
        "language": language,
        "supported": language in VOICE_LANGUAGE_CODES
    }