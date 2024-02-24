import reflex as rx
from alejoide.styles.colors import Text
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.components import images


def title() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.text("Hola, soy"),
        rx.chakra.text(
            "Alejo Sarmiento",
            color=Text.ACCENT.value,
            font_weight="bold",
            font_size=Size.XXLARGE.value,
            white_space="nowrap",
        ),
        rx.chakra.text(
            rx.chakra.span("SRE", font_weight="semibold"),
            rx.chakra.span(" y "),
            rx.chakra.span("Desarrollador de software", font_weight="semibold")
        ),
        font_size=[
            Size.NORMAL.value,
            Size.NORMAL.value,
            Size.NORMAL.value,
            Size.LARGE.value,
            Size.LARGE.value
        ],
    )


def header() -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.flex(
            title(),
            images.profile(
                "./me.jpeg",
                alt_text="Foto personal de Alejo Sarmiento",
                margin_top=[
                    Size.XXLARGE.value,
                    Size.XXLARGE.value,
                    Size.XXLARGE.value,
                    0,
                    0
                ],
            ),
        ),
        style=styles.HEADER,
    )