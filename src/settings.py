import os

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8011"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
