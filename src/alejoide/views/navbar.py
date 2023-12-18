import reflex as rx
from alejoide.modules.constants import Links
from alejoide.styles.sizes import Size
from alejoide.styles import styles
from alejoide.components.logo import logo


def buttons(**args) -> rx.Component:
    return rx.hstack(
        rx.link("Inicio", href=Links.HOME.value),
        rx.link("Sobre mí", href=Links.ABOUT.value),
        rx.link("Proyectos", href=Links.PROJECTS.value),
        rx.link("Contacto", href=Links.CONTACT.value),
        gap=Size.LARGE.value
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            logo(),
            buttons()
        ),
        style=styles.NAVBAR,
    )