import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.styles import colors


def profile(
        asset: str,
        alt_text: str = "",
        border_size: Size = Size.XXSMALL.value,
        border_color: colors.Main = colors.Main.PRIMARY.value,
        **args
    ) -> rx.Component:
    return rx.chakra.image(
        src=asset,
        alt=alt_text,
        width="30em",
        height="auto",
        border_radius="50%",
        overflow="hidden",
        border=f"{border_size} solid {border_color}",
        object_fit="cover",
        **args
    )