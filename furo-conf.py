# # flake8: noqa
# # Configuration file for the Sphinx documentation builder.
# #
# # This file only contains a selection of the most common options. For a full
# # list see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html

# # -- Path setup --------------------------------------------------------------

# # If extensions (or modules to document with autodoc) are in another directory,
# # add these directories to sys.path here. If the directory is relative to the
# # documentation root, use os.path.abspath to make it absolute, like shown here.
# #
# import os
# import sys
# sys.path.insert(0, os.path.abspath("./"))

# from fugue import __version__

# # -- Project information -----------------------------------------------------

# project = "Fugue Tutorials"
# version = __version__
# copyright = "2021, The Fugue Development Team"  # noqa: A001
# author = "The Fugue Development Team"


# # -- General configuration ---------------------------------------------------

# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode",
#               "sphinx.ext.autodoc", "sphinx_rtd_theme",
#               "nbsphinx","sphinx.ext.mathjax", "myst_parser"]

# nbsphinx_execute = 'never'

# nbsphinx_toctree = {
#   "maxdepth": 2
# }

# # Add any paths that contain templates here, relative to this directory.
# templates_path = ["docs/_templates"]

# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ["venv"]


# # -- Options for HTML output -------------------------------------------------

# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# html_theme = "furo"

# # This is the sidebar title
# html_title = "Fugue Tutorials"

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["docs/_static"]
# html_logo = "docs/_static/logo_blue.svg"

# # navigation_depth is supported in sphinx readthedocs theme but not furo
# html_theme_options = {
#     # "light_css_variables": {
#     #     "color-brand-primary": "red",
#     #     "color-brand-content": "#CC3333",
#     #     "color-admonition-background": "orange",
#     # },
#     "light_css_variables": {
#         "color-brand-primary": "#254262",
#         "color-brand-content": "#254262",
#         "color-api-highlight-on-target": "#6081a6",
#     },
#     "dark_css_variables": {
#         "color-foreground-primary": "black",
#         "color-foreground-secondary": "#5a5c63",
#         "color-foreground-muted": "#72747e",
#         "color-foreground-border": "#878787",
#         "color-background-primary": "white",
#         "color-background-secondary": "#f8f9fb",
#         "color-background-hover": "#efeff4ff",
#         "color-background-hover--transparent": "#efeff400",
#         "color-background-border": "#eeebee",
#         "color-admonition-background": "transparent",
#         "color-api-highlight-on-target": "#e5fff5",
#     },

# }
# html_favicon = "docs/_static/fugue_logo_trimmed.svg"

# # Adding .ipynb here crashes nbsphinx
# source_suffix = {'.md': 'markdown'}

# master_doc = 'index'
