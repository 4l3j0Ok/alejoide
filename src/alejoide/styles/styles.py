from alejoide.styles.fonts import Fonts
from alejoide.styles.colors import Color, TextColor
from alejoide.styles.sizes import Size
from enum import Enum


STYLESHEETS = [
    f"https://fonts.googleapis.com/css?family={Fonts.DEFAULT.value}&display=swap",
]

BASE_STYLE = {}
BASE_STYLE["background_color"] = Color.PRIMARY.value
BASE_STYLE["font_family"] = Fonts.DEFAULT.value
BASE_STYLE["font_size"] = Size.NORMAL.value
BASE_STYLE["color"] = TextColor.PRIMARY.value