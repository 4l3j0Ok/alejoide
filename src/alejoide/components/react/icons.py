import reflex as rx


# Search for icons here: https://icon-sets.iconify.design/
class Iconify(rx.Component):
    library = "@iconify/react"
    tag = "Icon"
    lib_dependencies: list[str] = ["@iconify/react"]
    icon: rx.Var[str]

    @classmethod
    def create(self, icon: str, **args):
        component = super().create(**args)
        component.icon = icon
        return component


def iconify(icon: str, **args) -> rx.chakra.Span:
    return rx.chakra.span(
        Iconify().create(icon),
        display="inline-block",
        vertical_align="middle",
        **args
    )
