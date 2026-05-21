from product_detection import detect_product_from_text, detect_quantity


def speech_to_text_mock(audio_file):
    return {
        "status": "success",
        "text": "customer ordered 10 sugar and 5 oil"
    }


def process_voice_order(audio_file):
    text_result = speech_to_text_mock(audio_file)
    order_text = text_result["text"]

    products = detect_product_from_text(order_text)
    quantities = detect_quantity(order_text)

    return {
        "status": "success",
        "order_text": order_text,
        "products": products["detected_products"],
        "quantities": quantities["quantities"],
        "message": "Voice order processed successfully"
    }