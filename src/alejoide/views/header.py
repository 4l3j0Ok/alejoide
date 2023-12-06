import reflex as rx
from alejoide.styles.colors import Color, TextColor
from alejoide.styles import styles
from alejoide.modules.constants import App, Links
from alejoide.styles.sizes import Size


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
            rx.image(
                src="./me.jpeg",
                alt="Foto personal de Alejo Sarmiento.",
                width="30em",
                height="auto",
                border_radius="50%",
                overflow="hidden",
                border=f"{Size.XSMALL.value} solid {Color.TERCEARY.value} ",
                object_fit="cover",
            ),
            padding_top=Size.XXLARGE.value,
            align_items="center",
            justify_content="space-between",
            flex_wrap="wrap",
            style=styles.WIDTH_STYLE,
        )
    )