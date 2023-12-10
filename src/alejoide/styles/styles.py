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
    rx.Flex: {
        "width": "100%",
        "max_width": "1200px",
        "justify_content": "space-between",
        "align_items":"center",
        "flex_wrap":"wrap",
    },
    rx.Link: {
        ":hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none",
        },
    },
    rx.Heading: {
        "font_family": Font.DEFAULT.value
    }
}

NAVBAR_KEYFRAME = {
    "to": {
        "backdrop_filter": "blur(5px)",
        "font_size": Size.SMALL.value,
        "color": "TextColor.SECONDARY.value",
    }
}

NAVBAR_STYLE = {
    "background": Color.SECONDARY.value,
    "padding_y": Size.NORMAL.value,
    "position": "sticky",
    "top": 0,
    "animation": "test linear both",
    "animation-timeline": "scroll(root)",
    "animation-range": "0 300px",
    "@keyframes test": NAVBAR_KEYFRAME,
}

