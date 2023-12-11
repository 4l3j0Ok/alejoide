import reflex as rx
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.styles import colors
from alejoide.modules.constants import AboutMe
from alejoide.modules.utils import hex_to_rgba


def cards() -> rx.Component:
    cards = []
    for item in AboutMe.CARDS.value:
        cards.append(
            rx.card(
                body=rx.box(*[rx.text(line) for line in item["body"]]),
                header=rx.text(
                    rx.span(
                        class_name=item["icon"],
                        margin_right=Size.SMALL.value,
                        color=colors.Text.TERCEARY.value,
                    ),
                    rx.span(
                        item["title"],
                        font_weight="bold"
                    ),
                    font_size=Size.LARGE.value,
                ),
                box_shadow=f"5px 5px 5px {hex_to_rgba(colors.Main.SECONDARY.value, 0.2)}",
                border=f"2px solid {hex_to_rgba(colors.Main.SECONDARY.value, 0.1)}",
                min_height="20em",
                height="auto",
            )
        )
    return rx.responsive_grid(
        *[rx.box(card) for card in cards],
        columns=[2],
        spacing=Size.LARGE.value,
        )


def about_me() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading(
                    "Sobre mí",
                ),
                rx.box(
                    *[rx.text(line) for line in AboutMe.DESCRIPTION.value],
                ),
            ),
        ),
        rx.flex(
            rx.box(
                rx.heading(
                    "Mis áreas de trabajo",
                    size="lg",
                ),
                cards()
            )
        ),
        id="about_me",
    )