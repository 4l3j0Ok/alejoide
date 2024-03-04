import os
import reflex as rx


config = rx.Config(
    app_name="alejoide",
    cors_allowed_origins=[os.getenv("APP_URL", "http://localhost:3000")]
)