import os
import reflex as rx


config = rx.Config(
    app_name="alejoide",
    cors_allowed_origins=os.environ.get("ALLOWED_ORIGINS", "*").split(","),
)