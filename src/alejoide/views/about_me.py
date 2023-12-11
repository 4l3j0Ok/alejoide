import reflex as rx
from alejoide.styles.sizes import Size
from alejoide.modules.constants import AboutMe
from alejoide.components.cards import card



def cards() -> rx.Component:
    cards = []
    for item in AboutMe.CARDS.value:
        cards.append(
            card(
                body=rx.box(*[rx.text(line) for line in item["body"]]),
                title=item["title"],
                icon=item["icon"],
            )
        )
    return rx.responsive_grid(
        *[rx.box(card) for card in cards],
        columns=[2],
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
                cards()
            )
        ),
        id="about_me",
    )