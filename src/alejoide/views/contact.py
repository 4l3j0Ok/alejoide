import reflex as rx
from alejoide.modules.constants import Links, Email
from alejoide.modules.utils import send_mail
from alejoide.styles import styles
from alejoide.components import forms
from alejoide.styles.sizes import Size


class FormState(rx.State):
    name: str
    email: str
    message: str
    # Form props
    submit_label: str = "Enviar"
    # Form state
    sent: bool = False
    loading: bool = False

    @rx.background
    async def send(self, form_data: dict) -> bool:
        async with self:
            self.loading = True
        success = send_mail(form_data)
        if success:
            async with self:
                self.sent = True
                self.loading = False
                self.submit_label = "¡Gracias por contactarte!"

    @rx.var
    def is_email_invalid(self) -> bool:
        return self.email and not ("@" in self.email and "." in self.email)

    @rx.var
    def is_name_invalid(self) -> bool:
        return self.name and len(self.name) < 3



def form() -> rx.Form:
    return rx.form(
        rx.hstack(
            rx.form_control(
                forms.input(
                    key="name",
                    label="Nombre",
                    placeholder="Tu nombre",
                    on_blur=FormState.set_name,
                    is_disabled=(FormState.sent | FormState.loading),
                ),
                rx.cond(
                    FormState.is_name_invalid,
                    rx.form_error_message("Ingresa un nombre válido."),
                ),
                is_invalid=FormState.is_name_invalid,
                is_required=True,
            ),
            rx.form_control(
                forms.input(
                    key="email",
                    label="Correo electrónico",
                    placeholder="Tu correo electrónico",
                    on_blur=FormState.set_email,
                    is_disabled=(FormState.sent | FormState.loading)
                ),
                rx.cond(
                    FormState.is_email_invalid,
                    rx.form_error_message("Ingresa un email válido."),
                ),
                is_invalid=FormState.is_email_invalid,
                is_required=True
            ),
            align_items="flex-start",
        ),
        rx.form_control(
            forms.text_area(
                key="message",
                label="Mensaje",
                placeholder="Escribí tu mensaje acá",
                is_disabled=(FormState.sent | FormState.loading),
                on_blur=FormState.set_message
            ),
            is_required=True
        ),
        forms.button(
            FormState.submit_label,
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
                    Email.ADDRESS.value,
                    href=Links.EMAIL.value,
                    as_="b",
                    color=styles.colors.Main.ACCENT.value
                )
            )
        ),
        id="contact",
    )
