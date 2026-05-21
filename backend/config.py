import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # Security
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "ai-wholesale-secret"
    )

    # Server Settings
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5000

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///wholesale.db"
    )

    # Upload Folders
    UPLOAD_FOLDER = "uploads"

    PRODUCT_UPLOAD_FOLDER = "uploads/products"
    INVOICE_UPLOAD_FOLDER = "uploads/invoices"
    RECEIPT_UPLOAD_FOLDER = "uploads/receipts"
    QR_UPLOAD_FOLDER = "uploads/qr"
    VOICE_ORDER_FOLDER = "uploads/voice-orders"

    # Max File Upload Size = 50 MB
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024

    # Default ERP Settings
    DEFAULT_LANGUAGE = "Hindi"

    BUSINESS_OPEN_TIME = "08:00"
    BUSINESS_CLOSE_TIME = "20:00"

    # Payment Settings
    UPI_ID = os.getenv("UPI_ID", "")
    QR_PAYMENT_ENABLED = True

    # WhatsApp Settings
    WHATSAPP_ENABLED = True
    WHATSAPP_NUMBER = os.getenv(
        "WHATSAPP_NUMBER",
        ""
    )

    # AI Settings
    AI_ENABLED = True