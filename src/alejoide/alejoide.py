import reflex as rx
from alejoide.views.navbar import navbar
from alejoide.views.header import header
from alejoide.styles import styles
from alejoide.styles.sizes import Size


def index() -> rx.Component:
    return rx.box(
        navbar(),
        header(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(index)
app.compile()
