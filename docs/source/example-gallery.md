# Example Gallery

This gallery contains a collection of code snippets together with their corresponding output, illustrating different 
functionalities all across the library.

```{tip}
This gallery is not the only place in our documentation where you can see explicit code and video examples: there are many more in our reference manual – see, for example, our documentation for the modules TODO and many more.

Check out our interactive Jupyter environment which allows running the examples online, without requiring a local installation.
```

```{eval-rst}
.. manim:: NerdfontIconMinimalExample
    :save_last_frame:
    
    
    import manim as m
    from manim_nerdfont_icons.icons import nerdfont_icon

    class NerdfontIconMinimalExample(m.Scene):

        def construct(self):
            self.camera.background_color = "#ece6e2"
            
            icon = nerdfont_icon("language-python", color=m.BLUE)
            self.add(icon)
    
```




