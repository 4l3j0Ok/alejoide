import reflex as rx


def button(label = "", **args) -> rx.Button:
    return rx.button(
        label,
        class_name="button is-primary",
        variant="solid",
        color_scheme="pink",
        **args
    )
