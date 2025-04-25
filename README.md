### Documentation

This project uses `sphinx` for generating the documentation.
It also uses a lot of sphinx extensions to make the documentation more readable and interactive.
For example the extension `myst-parser` is used to enable markdown support in the documentation (instead of the usual .rst-files).
It also uses the `sphinx-autobuild` extension to automatically rebuild the documentation when changes are made.
By running the following command, the documentation will be automatically built and served, when changes are made (make sure to run this command in the root directory of the project):

```shell
sphinx-autobuild ./docs/source/ ./docs/build/html/
```

This project features most of the extensions featured in this Tutorial: [Document Your Scientific Project With Markdown, Sphinx, and Read the Docs | PyData Global 2021](https://www.youtube.com/watch?v=qRSb299awB0).
