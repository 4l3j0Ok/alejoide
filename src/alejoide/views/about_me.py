import reflex as rx
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.styles.colors import Color, TextColor
from alejoide.modules.constants import AboutMe


def description() -> rx.Component:
    return rx.box(*[rx.text(description) for description in AboutMe.DESCRIPTION.value])


def about_me() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading(AboutMe.TITLE.value),
                description(),
            )
        ),
        margin_top=Size.XXXLARGE.value,
    )