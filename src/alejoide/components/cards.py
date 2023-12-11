import reflex as rx
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from alejoide.modules.utils import hex_to_rgba


def card(body = "", title = "", icon = "", **args) -> rx.Card:
    return rx.card(
        body=body,
        header=rx.text(
            rx.span(
                class_name=icon,
                margin_right=Size.SMALL.value,
                color=colors.Main.ACCENT.value,
            ),
            rx.span(
                title,
                font_weight="bold"
            ),
            font_size=Size.LARGE.value
        ),
        box_shadow=f"5px 5px 5px {hex_to_rgba(colors.Main.SECONDARY.value, 0.2)}",
        border=f"2px solid {hex_to_rgba(colors.Main.SECONDARY.value, 0.1)}",
        min_height="20em",
        height="auto",
        **args
    )