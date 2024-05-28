# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EPLWiki'
copyright = '2024, EPLStudents'
author = 'EPLStudents'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx_immaterial.task_lists', 'sphinxemoji.sphinxemoji']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_theme_options = {"navigation_with_keys": True}

def setup(app):
    app.add_css_file('css/custom.css')

# -- Options for LaTeX output ------------------------------
latex_engine = "xelatex"
latex_theme = "howto"
latex_elements = {"preamble": r"\setmainfont{Symbola}"}
