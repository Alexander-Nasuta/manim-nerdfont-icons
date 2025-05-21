import manim as m
from manim_nerdfont_icons.icons import nerdfont_icon


class NerdfontIconUnicodeExample(m.Scene):

    def construct(self):
        self.camera.background_color = "#ece6e2"

        icon = nerdfont_icon(983840, color=m.BLUE)

        self.add(icon)


if __name__ == '__main__':
    # Import manim library
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "NerdfontIconUnicodeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
