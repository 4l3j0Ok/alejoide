import yagmail
from alejoide.modules.constants import Email


def hex_to_rgba(hex: str, transparency: float = 1.0) -> str:
    hex = hex.lstrip("#")
    hlen = len(hex)
    return f"rgba({int(hex[hlen - 6:hlen - 4], 16)}, {int(hex[hlen - 4:hlen - 2], 16)}, {int(hex[hlen - 2:hlen], 16)}, {transparency})"


def send_mail(form_data) -> bool:
    yag = yagmail.SMTP(
        user=Email.ADDRESS.value,
        password=Email.TOKEN.value
    )
    user = form_data['name'].title()
    message = Email.MESSAGE_HEADER.value
    message += f"<b>Nombre</b>: {user}<br />"
    message += f"<b>Correo</b>: {form_data['email']}<br />"
    message += f"<b>Mensaje</b>:<br />"
    message += f"<p>{form_data['message']}</p>"
    try:
        yag.send(
            to=Email.PUBLIC_ADDRESS.value,
            subject=Email.SUBJECT.value,
            contents=message,
        )
        return True
    except Exception:
        return False
