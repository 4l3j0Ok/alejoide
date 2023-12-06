import reflex as rx
from alejoide.styles.fonts import Font
from alejoide.styles.colors import Color, TextColor
from alejoide.styles.sizes import Size
from enum import Enum


STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Font.DEFAULT.value}&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_size": Size.NORMAL.value,
    "color": TextColor.PRIMARY.value,
    "background_color": Color.PRIMARY.value,
    "animation": "fadeIn 1s ease-in-out",
    rx.Link: {
        "color": TextColor.PRIMARY.value,
        ":hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none",
        },
    },
}

WIDTH_STYLE = {}
WIDTH_STYLE["width"] = "80%"
WIDTH_STYLE["max_width"] = "1200px"