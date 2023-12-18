import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.modules.constants import Projects
from alejoide.components.cards import card_with_image
from alejoide.components.buttons import button


def add_button(
        buttons: list,
        text: str,
        url: str,
        icon: str
    ):
    buttons.append(
                rx.link(
                    button(
                        rx.text(
                            rx.span(
                                class_name=icon,
                                margin_right=Size.SMALL.value
                            ),
                            rx.span(text),
                        ),
                        width="100%"
                    ),
                    href=url,
                )
            )


def cards(**args) -> rx.Component:
    cards = []
    for item in Projects.CARDS.value:
        buttons = []
        if item.get("repo_url"):
            add_button(
                buttons,
                text=Projects.GITHUB_BUTTON.value["text"],
                url=item.get("repo_url"),
                icon=Projects.GITHUB_BUTTON.value["icon"]
            )
        if item.get("app_url"):
            add_button(
                buttons,
                text=Projects.APP_BUTTON.value["text"],
                url=item.get("app_url"),
                icon=Projects.APP_BUTTON.value["icon"]
            )
        cards.append(
            card_with_image(
                description=item.get("description"),
                title=item.get("title"),
                icon=item.get("icon"),
                image=item.get("image"),
                buttons=buttons
            )
        )
    return rx.responsive_grid(
        *[rx.box(card, **args) for card in cards],
        columns=[1, 1, 2, 2, 2],
        spacing=Size.XLARGE.value,
        )



def projects() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading("Proyectos"),
                rx.text(
                    "Aquí hay algunos de mis proyectos personales."
                )
            ),
            cards()
        )
    )