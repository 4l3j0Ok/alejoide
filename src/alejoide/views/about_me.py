import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.modules.constants import AboutMe
from alejoide.components.cards import card
from alejoide.styles import styles



def cards(**args) -> rx.Component:
    cards = []
    for item in AboutMe.CARDS.value:
        cards.append(
            card(
                description=rx.box(*[rx.text(line) for line in item.get("description", "")]),
                title=item.get("title"),
                icons=item.get("icons"),
            )
        )
    return rx.responsive_grid(
        *[rx.box(card, **args) for card in cards],
        columns=[1, 1, 1, 2, 2],
        spacing=Size.LARGE.value,
        )


def about_me() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.box(
                rx.heading(
                    "Sobre mí",
                ),
                rx.box(
                    *[rx.text(line) for line in AboutMe.DESCRIPTION.value],
                ),
            ),
        ),
        rx.flex(
            rx.box(
                rx.heading(
                    "Mis áreas de trabajo",
                    size="lg",
                ),
                cards(),
            )
        ),
        id="about_me",
    )