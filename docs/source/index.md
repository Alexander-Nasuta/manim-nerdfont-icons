# Manim Nerd Font Icons

```{tip}
Check out the Example Gallery for a collection of code snippets together with their corresponding output.
```

```{tip}
Have a look at the [Nerd Font Cheat Sheet](https://www.nerdfonts.com/cheat-sheet) for a list of all available icons.
```

```{eval-rst}
.. manim:: NerdfontIconExample
    :save_last_frame:
    
    
    import manim as m
    from manim_nerdfont_icons.icons import nerdfont_icon

    class NerdfontIconExample(m.Scene):

        def construct(self):
            
            icon = nerdfont_icon("language-python")
            self.add(icon)
    
```

# Readme

```{include} ../../README.md
:relative-images:
```



```{toctree}
:caption: 'Contents:'
:maxdepth: 2

example-gallery
icon-gallery
```
