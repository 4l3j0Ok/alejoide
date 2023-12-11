import reflex as rx
from alejoide.modules.constants import App, Links
from alejoide.styles.sizes import Size


def logo(clickable = True) -> rx.Component:
    return rx.link(
        App.NAME.value.upper(),
        href=Links.HOME.value,
        font_size=Size.LARGE.value,
        font_weight="semibold",
        letter_spacing=Size.XXSMALL.value
    ) if clickable else rx.box(
        App.NAME.value.upper(),
        font_size=Size.LARGE.value,
        font_weight="semibold",
        letter_spacing=Size.XXSMALL.value
    )