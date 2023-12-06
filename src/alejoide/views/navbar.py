import reflex as rx
from alejoide.modules.constants import App, Links
from alejoide.styles.colors import Color, TextColor
from alejoide.styles.sizes import Size
from alejoide.styles import styles


def buttons() -> rx.Component:
    return rx.hstack(
        rx.link("Inicio", href=Links.HOME.value),
        rx.link("Sobre mí", href=Links.ABOUT.value),
        rx.link("Proyectos", href=Links.PROJECTS.value),
        rx.link("Contacto", href=Links.CONTACT.value),
        gap=Size.LARGE.value,
    )


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.link(App.NAME.value.upper(),
                    href=Links.HOME.value,
                    font_size=Size.MEDIUM.value,
                    font_weight="semibold",
                    letter_spacing=Size.XSMALL.value
                ),
            ),
            rx.box(
                buttons()
            ),
            justify_content="space-between",
            align_items="center",
            flex_wrap="wrap",
            style=styles.WIDTH_STYLE,
        ),
        background_color=Color.SECONDARY.value,
        padding_y=Size.NORMAL.value,
    )