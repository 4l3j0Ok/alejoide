import reflex as rx
from alejoide.styles.colors import TextColor
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.components import images


def header() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.text("Hola, soy"),
                rx.span(
                    "Alejo Sarmiento",
                    color=TextColor.ACCENT.value,
                    font_weight="bold",
                    font_size=Size.XLARGE.value
                ),
                rx.text(
                    rx.span("SRE", font_weight="semibold"),
                    rx.span(" y "),
                    rx.span("Desarrollador de software", font_weight="semibold")
                ),
                font_size=Size.MEDIUM.value,
            ),
            images.profile("./me.jpeg", alt_text="Foto personal de Alejo Sarmiento"),
            margin_top=Size.XXLARGE.value,
            align_items="center",
            justify_content="space-between",
            flex_wrap="wrap",
            style=styles.WIDTH_STYLE,
        ),
    )