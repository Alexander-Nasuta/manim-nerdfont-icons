import manim as m
from manim_nerdfont_icons.icons import nerdfont_icon


class NerdfontIconOverview(m.Scene):

    def construct(self):

        no_rows = 6
        no_cols = 5

        from manim_nerdfont_icons.icons_dict import SYMBOLS_UNICODE

        icon_key_list = list(SYMBOLS_UNICODE.keys())

        def icon_group(idx):
            icon_name = icon_key_list[idx]
            icon_unicode = SYMBOLS_UNICODE[icon_name]

            m_symbol = nerdfont_icon(icon_unicode, font_size=20)
            m_name = m.Text(icon_name, font_size=15, font="DejaVu Sans Mono")
            m_unicode =  m.Text(
                f"0x{icon_unicode:04X}",
                font_size=15,
                font="DejaVu Sans Mono",
                color=m.BLUE
            )

            m_name.move_to(m.DOWN * 0.35)
            m_unicode.move_to(m.DOWN * 0.6)

            return m.VGroup(m_symbol, m_name, m_unicode)

        offset = 7331
        table_content = [
            [
                icon_group(idx=i * no_cols + j + offset) for j in range(no_cols)
            ] for i in range(no_rows)
        ]
        table = m.MobjectTable(
            table_content,
            v_buff=0.1,
            h_buff=0.1,
            # don't show v adn h lines
            line_config={"stroke_width": 0},
        )

        self.play(
            m.FadeIn(table),
        )


if __name__ == '__main__':
    # Import manim library
    import os
    from pathlib import Path

    # FLAGS = "-s --disable_caching"
    FLAGS = "-pqm"
    SCENE = "NerdfontIconOverview"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
