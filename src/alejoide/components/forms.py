import reflex as rx
from alejoide.styles import colors
from alejoide.styles import styles
from alejoide.modules.utils import hex_to_rgba


def input(key: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.text(label, html_for=key),
        rx.input(
            name=key,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        )
    )


def text_area(key: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.text(label, html_for=key),
        rx.text_area(
            name=key,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        )
    )


def button(label: str = "", **args) -> rx.Button:
    return rx.button(
        label,
        class_name="button is-primary",
        variant="solid",
        style=styles.FORM_COMPONENTS,
        color_scheme="pink",
        **args
    )
