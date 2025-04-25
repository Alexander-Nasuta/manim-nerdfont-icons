# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'manim-nerdfont-icons'
copyright = '2025, Alexander Nasuta'
author = 'Alexander Nasuta'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx_copybutton",

    "sphinx.ext.autosectionlabel",

    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",

    "sphinx.ext.autodoc",

    "sphinx.ext.napoleon",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",

    "manim_nerdfont_icons.docbuild.manta_directive",
]

templates_path = ['_templates']
exclude_patterns = []




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    'manim.css',
]
