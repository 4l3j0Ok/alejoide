import reflex as rx
from alejoide.styles.fonts import Font
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from enum import Enum

# Google Fonts and Font Awesome
STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Font.DEFAULT.value}&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
]


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_size": Size.NORMAL.value,
    "color": colors.Text.PRIMARY.value,
    "background": colors.Main.PRIMARY.value,
    "animation": "fadeIn 1s ease-in-out",
    rx.Flex: {
        "width": "100%",
        "max_width": "1200px",
        "justify_content": "space-between",
        "align_items":"center",
        "flex_direction": ["column", "column", "columns", "row", "row"],
        "flex_wrap": "wrap",
    },
    rx.Link: {
        "scroll_behavior": "smooth",
        ":hover": {
            "color": colors.Text.ACCENT.value,
            "text_decoration": "none",
        },
    },
    rx.Heading: {
        "font_family": Font.DEFAULT.value,
        "margin_y": Size.NORMAL.value,
    },
}

# NAVBAR STYLE

NAVBAR_KEYFRAME = {
    "to": {
        "font_size": Size.SMALL.value,
    }
}

NAVBAR_STYLE = {
    "background": colors.Header.SECONDARY.value,
    "color": colors.Text.SECONDARY.value,
    "padding_y": Size.LARGE.value,
    "position": "sticky",
    "top": 0,
    "animation": "test linear both",
    "animation-timeline": "scroll(root)",
    "animation-range": "0 300px",
    "@keyframes test": NAVBAR_KEYFRAME,
    "z_index": 1,
}

# HEADER STYLE

HEADER_STYLE = {
    "height": "95vh",
    "justify_content": "center",
    "background": colors.Header.PRIMARY.value,
    "color": colors.Text.SECONDARY.value,
}
