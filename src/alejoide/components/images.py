import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.styles.colors import Color


def profile(
        asset: str,
        alt_text: str = "",
        border_size: Size = Size.XSMALL.value,
        border_color: Color = Color.TERCEARY.value
    ) -> rx.Component:
    return rx.image(
        src=asset,
        alt=alt_text,
        width="30em",
        height="auto",
        border_radius="50%",
        overflow="hidden",
        border=f"{border_size} solid {border_color} ",
        object_fit="cover",
    )