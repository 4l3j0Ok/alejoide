import reflex as rx
from alejoide.views.navbar import navbar
from alejoide.views.header import header
from alejoide.views.about_me import about_me
from alejoide.styles import styles
from alejoide.styles.sizes import Size


def index() -> rx.Component:
    return rx.box(
        rx.script(src="https://kit.fontawesome.com/ed6fce8479.js"),
        navbar(),
        header(),
        about_me(),
        # projects(),
        # contact(),
        # footer(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(index)
app.compile()
