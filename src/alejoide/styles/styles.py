import reflex as rx
from alejoide.styles.fonts import Font
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from alejoide.modules.utils import hex_to_rgba

# Google Fonts and Font Awesome
STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Font.DEFAULT.value}&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
]


BASE = {
    "font_family": Font.DEFAULT.value,
    "font_size": Size.NORMAL.value,
    "color": colors.Text.PRIMARY.value,
    "background": colors.Main.PRIMARY.value,
    "animation": "fadeIn 1s ease-in-out",
    rx.Flex: {
        "width": "80%",
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
        }
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
    "background": colors.Main.TERCEARY.value,
    "justify_content": "center",
    "padding_y": Size.LARGE.value,
    "position": "sticky",
    "top": 0,
    "animation": "minimize linear both",
    "animation_timeline": "scroll(root)",
    "animation_range": "95vh 125vh",
    "a": DARK_LINKS,
    "@keyframes minimize": {
        "to": {
            "font_size": Size.SMALL.value,
            "background": hex_to_rgba(colors.Main.SECONDARY.value, 0.8),
            "backdrop-filter": "blur(5px)",
        }
    },
    "z_index": 2,
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
    "justify_content": "center",
}


FORM_COMPONENTS = {
    "width": "100%",
    "padding_y": Size.NORMAL.value,
}

ABOUT_ME_CARDS = {	
    "transition": "transform 0.2s ease-in-out",
    "transition_delay": "0.2s",
    ":hover": {
        "transform": f"scale(1.05)",
    }
}