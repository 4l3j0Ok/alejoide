import reflex as rx
from alejoide.styles import colors
from alejoide.modules.utils import hex_to_rgba


def input(input_id: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.form_label(label, html_for=input_id),
        rx.input(
            name=input_id,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
        ),
        **args
    )


def text_area(input_id: str = "", label: str = "", placeholder: str = "", **args) -> rx.Box:
    return rx.box(
        rx.form_label(label, html_for=input_id),
        rx.text_area(
            name=input_id,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
        ),
        **args
    )


def button(label: str = "", type: str = "", **args) -> rx.Button:
    return rx.button(
        label,
        type_=type,
        class_name="button is-primary",
        variant="solid",
        **args
    )