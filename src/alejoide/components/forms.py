import reflex as rx
from alejoide.styles import colors
from alejoide.modules.utils import hex_to_rgba


def input(key: str = "", label: str = "", placeholder: str = "", **args) -> rx.chakra.Box:
    return rx.chakra.box(
        rx.chakra.text(label, html_for=key),
        rx.chakra.input(
            name=key,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        )
    )


def text_area(key: str = "", label: str = "", placeholder: str = "", **args) -> rx.chakra.Box:
    return rx.chakra.box(
        rx.chakra.text(label, html_for=key),
        rx.chakra.text_area(
            name=key,
            placeholder=placeholder,
            focus_border_color=hex_to_rgba(colors.Main.ACCENT.value, 0.5),
            **args
        )
    )
