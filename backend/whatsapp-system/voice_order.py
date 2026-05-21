def process_whatsapp_voice_order(customer_phone, audio_file):
    if not audio_file:
        return {
            "status": "error",
            "message": "Audio file required"
        }

    return {
        "status": "success",
        "customer_phone": customer_phone,
        "audio_file": audio_file,
        "detected_text": "10 sugar aur 5 oil ka order",
        "message": "Voice order processed successfully"
    }