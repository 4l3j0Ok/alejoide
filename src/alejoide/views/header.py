import reflex as rx
from alejoide.styles.colors import Text
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.components import images


def title() -> rx.Component:
    return rx.box(
        rx.text("Hola, soy"),
        rx.text(
            "Alejo Sarmiento",
            color=Text.ACCENT.value,
            font_weight="bold",
            font_size=Size.XXLARGE.value
        ),
        rx.text(
            rx.span("SRE", font_weight="semibold"),
            rx.span(" y "),
            rx.span("Desarrollador de software", font_weight="semibold")
        ),
        font_size=Size.LARGE.value,
    )


def header() -> rx.Component:
    return rx.hstack(
        rx.flex(
            title(),
            images.profile("./me.jpeg", alt_text="Foto personal de Alejo Sarmiento"),
        ),
        style=styles.HEADER,
    )