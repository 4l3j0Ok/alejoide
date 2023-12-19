import reflex as rx
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from alejoide.components.react.icons import iconify


def card(description = "", title = "", icons = "", buttons = [], **args) -> rx.Card:
    footer = rx.responsive_grid(
        *[button for button in buttons],
        columns=[1, 1, 1, 2, 2],
        spacing=Size.NORMAL.value,
        width="100%") if buttons else None
    return rx.card(
        body=description,
        header=rx.text(
            rx.span(
                title,
                font_weight="bold"
            ),
            *[
                iconify(
                    icon,
                    margin_left=Size.SMALL.value,
                    color=colors.Main.ACCENT.value
                ) for icon in icons.split("|")
            ],
            font_size=Size.LARGE.value
        ),
        min_height="20em",
        footer=footer,
        **args
    )


def card_with_image(description = "", title = "", icons = "", image = "", buttons = [], **args) -> rx.Card:
    pre_body = []
    pre_body.append(
        rx.image(
            src=image,
            border_radius="5px",
            width="100%",
            )
        ) if image else None
    pre_body.append(
        rx.heading(
            rx.span(
                title,
                font_weight="bold"
            ),
            *[
                iconify(
                    icon,
                    margin_left=Size.SMALL.value,
                    color=colors.Main.ACCENT.value,
                ) for icon in icons.split("|")
            ],
            justify_content="space-between",
            font_size=Size.LARGE.value,
        )
    )
    pre_body.append(rx.box(*[rx.text(line) for line in description]))
    body = rx.box(*[item for item in pre_body if item])
    footer = rx.responsive_grid(
        *[button for button in buttons],
        columns=[1, 1, 1, 2, 2],
        spacing=Size.NORMAL.value,
        width="100%") if buttons else None
    return rx.card(
        body=body,
        min_height="35em",
        footer=footer,
        **args
    )
