import reflex as rx
from alejoide.modules.constants import App, Links
from alejoide.styles.sizes import Size
from alejoide.styles import styles


def logo(clickable = True, on_dark = True) -> rx.Component:
    return rx.link(
        App.NAME.value.upper(),
        href=Links.HOME.value,
        font_size=Size.LARGE.value,
        font_weight="semibold",
        letter_spacing=Size.XXSMALL.value,
        style=styles.DARK_LINKS if on_dark else {}
    ) if clickable else rx.box(
        App.NAME.value.upper(),
        font_size=Size.LARGE.value,
        font_weight="semibold",
        letter_spacing=Size.XXSMALL.value,
    )