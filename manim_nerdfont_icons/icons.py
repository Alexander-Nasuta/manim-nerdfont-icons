import manim as m
from manim import Text

import manim_nerdfont_icons.resources
import importlib.resources as pkg_resources

from manim_nerdfont_icons.icons_dict import SYMBOLS_UNICODE


def nerdfont_icon(icon: int | str, **kwargs) -> Text:
    """
    Returns the Nerd Font icon for a given name.
    """
    with pkg_resources.path(manim_nerdfont_icons.resources, 'SymbolsNerdFontMono-Regular.ttf') as font_path:
        with m.register_font(str(font_path)):

            kwargs["font"] = "Symbols Nerd Font Mono"
            if isinstance(icon, str):
                if icon in SYMBOLS_UNICODE.keys():
                    return m.Text(chr(SYMBOLS_UNICODE[icon]), **kwargs)
                else:
                    return m.Text(icon, **kwargs)
            elif isinstance(icon, int):
                return m.Text(chr(icon), **kwargs)
            else:
                raise ValueError("icon must be int, str or chr")

