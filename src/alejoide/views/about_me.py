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
                description=rx.chakra.box(*[rx.chakra.text(line) for line in item.get("description", "")]),
                title=item.get("title"),
                icons=item.get("icons"),
            )
        )
    return rx.chakra.responsive_grid(
        *[rx.chakra.box(card, **args) for card in cards],
        columns=[1, 1, 1, 2, 2],
        spacing=Size.LARGE.value,
        )


def about_me() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.flex(
            rx.chakra.box(
                rx.chakra.heading(
                    "Sobre mí",
                ),
                rx.chakra.box(
                    *[rx.chakra.text(line) for line in AboutMe.DESCRIPTION.value],
                ),
            ),
        ),
        rx.chakra.flex(
            rx.chakra.box(
                rx.chakra.heading(
                    "Mis áreas de trabajo",
                    size="lg",
                ),
                cards(),
            )
        ),
        id="about_me",
    )