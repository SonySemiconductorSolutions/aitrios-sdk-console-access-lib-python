# ------------------------------------------------------------------------
# Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

# pylint:disable=redefined-builtin
# pylint:disable=invalid-name
# pylint:disable=unused-import
# pylint:disable=missing-module-docstring

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import os
import sys

sys.path.insert(0, os.path.abspath("../../../src"))
sys.path.insert(1, os.path.abspath("../../../src/console_access_library"))

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

# add modules as mock imports here, if any module gives import error.
autodoc_mock_imports = []
try:
    import aitrios_console_rest_client_sdk_primitive
    import marshmallow
    import streamlit

    import console_access_library
except ImportError:
    autodoc_mock_imports.append("marshmallow")
    autodoc_mock_imports.append("streamlit")

# -- Project information -----------------------------------------------------

project = "Console Access Library"
copyright = "2022 Sony Semiconductor Solutions Corp"
author = "SARD"

# The full version, including alpha/beta/rc tags
release = "1.0.0"
version = "1.0.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "myst_parser",
    "rst2pdf.pdfbuilder",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
]

# sphinxcontrib.napoleon is an extension used to parse, both numpy and google formats of docstring.
# settings to include source code link at each module description, also include the extensions,
# "sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.intersphinx", "sphinx.ext.autosummary",
# to make this work.
autodoc_member_order = "bysource"

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
autosummary_generate = True

# latex and pdf generation (to remove blank pages generated after runing 'make latexpdf' command)
latex_elements = {
    "extraclassoptions": "openany,oneside",
    "preamble": r"""
    \usepackage[draft]{minted}
    \fvset{breaklines=true}
    \usepackage{makeidx}
    \usepackage{enumitem}
    \setlistdepth{99}
    \usepackage[columns=1]{idxlayout}
    \makeindex
    """,
}
latex_engine = "pdflatex"

# shorten the module names only to current module and not include the parent class details,
# if given as false
add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# flag to number images
numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
]
