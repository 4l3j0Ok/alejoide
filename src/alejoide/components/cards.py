import reflex as rx
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from alejoide.modules.utils import hex_to_rgba


def card(description = "", title = "", icon = "", **args) -> rx.Card:
    return rx.card(
        body=description,
        header=rx.text(
            rx.span(
                title,
                font_weight="bold"
            ),
            *[
                rx.span(
                    class_name=i,
                    margin_left=Size.SMALL.value,
                    color=colors.Main.ACCENT.value,
                ) for i in icon.split("|")
            ],
            font_size=Size.LARGE.value
        ),
        box_shadow=f"5px 5px 5px {hex_to_rgba(colors.Main.SECONDARY.value, 0.2)}",
        border=f"2px solid {hex_to_rgba(colors.Main.SECONDARY.value, 0.1)}",
        min_height="20em",
        height="auto",
        **args
    )


def card_with_image(description = "", title = "", icon = "", image = "", buttons = [], **args) -> rx.Card:
    pre_body = []
    pre_body.append(
        rx.image(
            src=image,
            border_radius="5px"
            )
        ) if image else None
    icons = [
        rx.span(
            class_name=i,
            margin_left=Size.SMALL.value,
            color=colors.Main.ACCENT.value,
        ) for i in icon.split("|") if icon 
    ]
    pre_body.append(
        rx.heading(
            rx.span(
                title,
                font_weight="bold"
            ),
            *icons,
            justify_content="space-between",
            font_size=Size.LARGE.value
        )
    )
    pre_body.append(rx.box(*[rx.text(line) for line in description]))
    body = rx.box(*[item for item in pre_body if item])
    footer = rx.responsive_grid(
        *[button for button in buttons],
        columns=[1, 1, 2, 2, 2],
        spacing=Size.NORMAL.value,
        width="100%") if buttons else None
    return rx.card(
        body=body,
        box_shadow=f"5px 5px 5px {hex_to_rgba(colors.Main.SECONDARY.value, 0.2)}",
        border=f"2px solid {hex_to_rgba(colors.Main.SECONDARY.value, 0.1)}",
        min_height="20em",
        height="auto",
        footer=footer,
        **args
    )
