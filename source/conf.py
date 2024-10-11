# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# At top on conf.py (with other import statements)
# import recommonmark
# from recommonmark.transform import AutoStructify


project = 'Knowledge Base for Goodix BLE'
copyright = '2024, Goodix'
author = 'nix.long'
release = 'v1.0'

from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = ['recommonmark','sphinx_markdown_tables']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': True,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "当页导航",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 12,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    # 'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "exclude", # 去掉打开源码的链接
}


# At the bottom of conf.py
# def setup(app):
#     app.add_config_value('recommonmark_config', {
#             'enable_math': True,
#             'enable_inline_math': True,
#             }, True)
#     app.add_transform(AutoStructify)

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "MyUserName", # Username
    "github_repo": "MyDoc", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}