import reflex as rx
from alejoide.modules.constants import Links
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.components.logo import logo


def buttons(**args) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.link("Inicio", href=Links.HOME.value),
        rx.chakra.link("Sobre mí", href=Links.ABOUT.value),
        rx.chakra.link("Proyectos", href=Links.PROJECTS.value),
        rx.chakra.link("Contacto", href=Links.CONTACT.value),
        gap=Size.LARGE.value,
        margin_top=[Size.NORMAL.value, Size.NORMAL.value, Size.NORMAL.value, 0],
    )


def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.flex(
            logo(),
            buttons()
        ),
        style=styles.NAVBAR,
    )