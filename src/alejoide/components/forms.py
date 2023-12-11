import reflex as rx
from alejoide.styles import colors
from alejoide.styles import styles
from alejoide.modules.utils import hex_to_rgba


def input(input_id: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.text(label, html_for=input_id),
        rx.input(
            name=input_id,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        ),
        style=styles.FORM_COMPONENTS
    )


def text_area(input_id: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.text(label, html_for=input_id),
        rx.text_area(
            name=input_id,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        ),
        style=styles.FORM_COMPONENTS
    )


def button(label: str = "", **args) -> rx.Button:
    return rx.button(
        label,
        class_name="button is-primary",
        variant="solid",
        style=styles.FORM_COMPONENTS,
        **args
    )
