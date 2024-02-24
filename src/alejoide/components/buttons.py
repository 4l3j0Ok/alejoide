import reflex as rx


def button(label = "", **args) -> rx.chakra.Button:
    return rx.chakra.button(
        label,
        class_name="button is-primary",
        variant="solid",
        color_scheme="pink",
        **args
    )
