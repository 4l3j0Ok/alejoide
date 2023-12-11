import reflex as rx
from alejoide.modules.constants import Links
from alejoide.styles import styles
from alejoide.components import forms
from alejoide.styles.sizes import Size


def form() -> rx.Form:
    return rx.form(
        rx.hstack(
            forms.input("name", "Nombre", "Tu nombre", width="100%"),
            forms.input("email", "Correo electrónico", "Tu correo electrónico", width="100%"),
        ),
        forms.text_area("message", "Mensaje", "Escribí tu mensaje acá"),
        forms.button("Enviar", margin_top=Size.NORMAL.value)
    )

def contact() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading("Contacto"),
                rx.text("Hablemos, escribime un mensaje y te respondo lo más pronto posible."),
            ),
        ),
        rx.flex(
            rx.box(
                form(),
                width="100%"
                )
            ),
        rx.flex(
            rx.text(
                "O si preferís, podes escribirme a mi correo electrónico: ",
                rx.link(
                    Links.EMAIL.value.replace("mailto:", ""),
                    href=Links.EMAIL.value,
                    as_="b",
                    color=styles.colors.Main.ACCENT.value
                )
            )
        ),
        spacing=Size.LARGE.value,
        id="contact"
    )
