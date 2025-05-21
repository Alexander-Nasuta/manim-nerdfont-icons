# Example Gallery

This gallery contains a collection of code snippets together with their corresponding output, illustrating different ways to create nerd font icons in Manim.



```{eval-rst}
.. manim:: NerdfontIconMinimalExample
    :save_last_frame:
    
    
    import manim as m
    from manim_nerdfont_icons.icons import nerdfont_icon

    class NerdfontIconMinimalExample(m.Scene):

        def construct(self):
            
            icon = nerdfont_icon("language-python", color=m.BLUE)
            self.add(icon)
    
```

```{tip}
Please have a look at the icon galelry to browse all available icons.
```

```{eval-rst}
.. manim:: NerdfontIconOverview
    :save_last_frame:
    
    
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
                m_name = m.Text(icon_name, font_size=15)
                m_unicode =  m.Text(
                    f"0x{icon_unicode:04X}",
                    font_size=15,
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
        import os
        from pathlib import Path

        FLAGS = "-pqm"
        SCENE = "NerdfontIconOverview"

        file_path = Path(__file__).resolve()
        os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")

```




```{eval-rst}
.. manim:: NerdfontIconUnicodeExample
    :save_last_frame:
    
    
    import manim as m
    from manim_nerdfont_icons.icons import nerdfont_icon

    class NerdfontIconUnicodeExample(m.Scene):

        def construct(self):
            
            icon = nerdfont_icon(983840, color=m.BLUE)
            self.add(icon)
    
```


```{eval-rst}
.. manim:: NerdfontIconUnicodeHexExample
    :save_last_frame:
    
    
    import manim as m
    from manim_nerdfont_icons.icons import nerdfont_icon

    class NerdfontIconUnicodeHexExample(m.Scene):

        def construct(self):
            
            icon = nerdfont_icon(0xF0320, color=m.BLUE)
            self.add(icon)
    
```



