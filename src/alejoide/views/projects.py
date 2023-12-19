import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.modules.constants import Projects
from alejoide.components.cards import card_with_image
from alejoide.components.buttons import button
from alejoide.components.react.icons import iconify


def add_button(
        buttons: list,
        text: str,
        url: str,
        icon: str,
        is_disabled: bool = False
    ):
    buttons.append(
        rx.link(
            button(
                rx.text(
                    iconify(
                        icon,
                        margin_right=Size.SMALL.value
                    ),
                    rx.span(text),
                ),
                width="100%",
                is_disabled=is_disabled
            ),
            href=url,
            is_external=True
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
                icon=Projects.APP_BUTTON.value["icon"],
                is_disabled=item.get("is_disabled", False)
            )
        cards.append(
            card_with_image(
                description=item.get("description"),
                title=item.get("title"),
                icons=item.get("icons"),
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
                rx.box(
                    *[rx.text(line) for line in Projects.DESCRIPTION.value],
                    margin_bottom=Size.LARGE.value,
                ),
            ),
            cards()
        ),
        id="projects"
    )