import os
import reflex as rx


config = rx.Config(
    app_name="alejoide",
    api_url=os.getenv("API_URL", "http://localhost:8000")
)