import reflex as rx
from alejoide.styles import styles


def button(label = "", **args) -> rx.Button:
    return rx.button(
        label,
        class_name="button is-primary",
        variant="solid",
        color_scheme="pink",
        **args
    )
