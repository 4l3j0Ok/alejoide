import os
import reflex as rx


config = rx.Config(
    app_name="alejoide",
    cors_allowed_origins=os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:3000").split(",")
)