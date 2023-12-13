import reflex as rx
from alejoide.views.navbar import navbar
from alejoide.views.header import header
from alejoide.views.about_me import about_me
from alejoide.views.footer import footer
from alejoide.views.contact import contact
from alejoide.styles import styles
from alejoide.styles.sizes import Size
from alejoide.modules.constants import App


@rx.page(route="/", title=App.NAME.value, description=App.DESCRIPTION.value)
def index() -> rx.Component:
    return rx.box(
        rx.script(src="https://kit.fontawesome.com/ed6fce8479.js"),
        navbar(),
        header(),
        rx.spacer(height=Size.XXXLARGE.value),
        about_me(),
        rx.spacer(height=Size.XXXLARGE.value),
        # projects(),
        # rx.spacer(height=Size.XXXLARGE.value),
        contact(),
        rx.spacer(height=Size.XXXLARGE.value),
        footer(),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE

)

app.compile()
