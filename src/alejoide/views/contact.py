import reflex as rx
from alejoide.modules.constants import Links
from alejoide.modules.contact import send_mail
from alejoide.styles import styles
from alejoide.components import forms
from alejoide.styles.sizes import Size


class FormState(rx.State):
    label: str = "Enviar"
    sent: bool = False
    loading: bool = False
    form_data: dict = {}

    @rx.background
    async def send(self, form_data: dict) -> bool:
        async with self:
            self.form_data = form_data
            self.loading = True
        success = send_mail(form_data)
        if success:
            async with self:
                self.sent = True
                self.loading = False
                self.label = "¡Gracias por contactarte!"


def form() -> rx.Form:
    return rx.form(
        rx.hstack(
            forms.input(
                input_id="name",
                label="Nombre",
                placeholder="Tu nombre",
                is_disabled=(FormState.sent | FormState.loading)
            ),
            forms.input(
                input_id="email",
                label="Correo electrónico",
                placeholder="Tu correo electrónico",
                is_disabled=(FormState.sent | FormState.loading)
            ),
        ),
        forms.text_area(
            input_id="message",
            label="Mensaje",
            placeholder="Escribí tu mensaje acá",
            is_disabled=(FormState.sent | FormState.loading),
        ),
        forms.button(
            FormState.label,
            type_="submit",
            is_loading=FormState.loading,
            is_disabled=FormState.sent,
            margin_top=Size.NORMAL.value,
        ),
        on_submit=FormState.send,
    )

def contact() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading("Contacto"),
                rx.text("Si querés contactarme, podés hacerlo a través de este formulario."),
            ),
        ),
        rx.flex(
            rx.box(
                form(),
                style=styles.FORM_COMPONENTS,
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
        id="contact",
    )
