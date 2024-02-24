import reflex as rx
from alejoide.styles.fonts import Font
from alejoide.styles import colors
from alejoide.styles.sizes import Size
from alejoide.modules.utils import hex_to_rgba


STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Font.DEFAULT.value}&display=swap"
]

BASE = {
    "font_family": f"{Font.DEFAULT.value} !important",
    "font_size": Size.NORMAL.value,
    "color": colors.Text.PRIMARY.value,
    "background": colors.Main.PRIMARY.value,
    "::selection": {
        "background": colors.Main.ACCENT.value,
        "color": colors.Text.SECONDARY.value,
    },
    "::moz_selection": {
        "background": colors.Main.ACCENT.value,
        "color": colors.Text.SECONDARY.value,
    },
    rx.chakra.Card: {
        "box_shadow": f"5px 5px 5px {hex_to_rgba(colors.Main.SECONDARY.value, 0.2)}",
        "border": f"2px solid {hex_to_rgba(colors.Main.SECONDARY.value, 0.1)}",
        "height": "auto"
    },
    rx.chakra.Flex: {
        "width": "80%",
        "max_width": "1200px",
        "justify_content": "space-between",
        "align_items":"center",
        "flex_direction": ["column", "column", "columns", "row", "row"],
        "flex_wrap": "wrap",
    },
    rx.chakra.Link: {
        "color": colors.Main.ACCENT.value,
        ":hover": {
            "color": colors.Text.PRIMARY.value,
            "text_decoration": "none",
        }
    },
    rx.chakra.Heading: {
        "font_family": f"{Font.DEFAULT.value} !important",
        "margin_y": Size.NORMAL.value,
    },
    rx.chakra.Button: {
        "background_color": colors.Main.ACCENT.value,
        "color": colors.Text.SECONDARY.value,
        ":hover": {
            "background_color": colors.Main.TERCEARY.value,
        }
    },
    rx.chakra.Image: {
        "pointerEvents": "none",
        "userSelect": "none",
    },
}

DARK_LINKS = {
    "color": colors.Text.SECONDARY.value,
    ":hover": {
        "color": colors.Text.ACCENT.value,
        "text_decoration": "none",
    },
}

NAVBAR = {
    "background": colors.Main.TERCEARY.value,
    "text_align": "center",
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
            "background": hex_to_rgba(colors.Main.TERCEARY.value, 0.8),
            "backdropFilter": "blur(5px)",
        }
    },
    "z_index": 2,
}

HEADER = {
    "height": "95vh",
    "justify_content": "center",
    "background": colors.Header.PRIMARY.value,
    "color": colors.Text.SECONDARY.value,
}

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

SCALE = {	
    "transition": "transform 0.2s ease-in-out",
    "transition_delay": "0.2s",
    ":hover": {
        "transform": f"scale(1.05)",
    }
}
