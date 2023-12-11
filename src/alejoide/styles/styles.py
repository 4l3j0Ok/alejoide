import reflex as rx
from alejoide.styles.fonts import Font
from alejoide.styles import colors
from alejoide.styles.sizes import Size

# Google Fonts and Font Awesome
STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Font.DEFAULT.value}&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
]


BASE = {
    "scroll_behavior": "smooth",
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
        "color": colors.Main.ACCENT.value,
        ":hover": {
            "color": colors.Text.PRIMARY.value,
            "text_decoration": "none",
        },
    },
    rx.Heading: {
        "font_family": Font.DEFAULT.value,
        "margin_y": Size.NORMAL.value,
    },
    rx.Button: {
        "background_color": colors.Main.ACCENT.value,
        "color": colors.Text.SECONDARY.value,
        ":hover": {
            "background_color": colors.Main.TERCEARY.value,
        }
    }
}

# FOR LINKS WHERE THE BACKGROUND IS DARK
DARK_LINKS = {
    "color": colors.Text.SECONDARY.value,
    ":hover": {
        "color": colors.Text.ACCENT.value,
        "text_decoration": "none",
    },
}

# NAVBAR STYLE

NAVBAR = {
    "background": colors.Header.SECONDARY.value,
    "color": colors.Text.SECONDARY.value,
    "justify_content": "center",
    "padding_y": Size.LARGE.value,
    "position": "sticky",
    "top": 0,
    "animation": "minimize linear both",
    "animation_timeline": "scroll(root)",
    "animation_range": "0 300px",
    "@keyframes minimize": {
        "to": {
            "font_size": Size.SMALL.value,
        }
    },
    "z_index": 1,
}

# HEADER STYLE

HEADER = {
    "height": "95vh",
    "justify_content": "center",
    "background": colors.Header.PRIMARY.value,
    "color": colors.Text.SECONDARY.value,
}


# FOOTER STYLE

FOOTER = {
    "color": colors.Text.SECONDARY.value,
    "background": colors.Main.TERCEARY.value,
    "width": "100%",
    "padding_y": Size.XXLARGE.value,
    "padding_x": Size.LARGE.value,
    "justify_content":"center",
}


FORM_COMPONENTS = {
    "width": "100%",
    "padding_y": Size.NORMAL.value,
}