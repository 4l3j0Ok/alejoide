import reflex as rx
from alejoide.styles.colors import Color, TextColor
from alejoide.modules.constants import App, Links
from alejoide.styles.sizes import Size


def buttons() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.link("Inicio", href=Links.HOME.value),
            rx.link("Sobre mí", href=Links.ABOUT.value),
            rx.link("Proyectos", href=Links.PROJECTS.value),
            rx.link("Contacto", href=Links.CONTACT.value),
            gap=Size.LARGE.value,
        ),
        font_size=Size.NORMAL.value
    )


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.link(App.NAME.value.upper(),
                    href=Links.HOME.value,
                    font_size=Size.MEDIUM.value,
                    font_weight="semibold",
                    letter_spacing=Size.XSMALL.value,
                )
            ),
            rx.box(
                rx.spacer(),
                buttons(),
                padding=Size.NORMAL.value
            ),
            justify_content="space-between",
            align_items="center",
            width="80%",
        ),
        background_color=Color.SECONDARY.value,
    )