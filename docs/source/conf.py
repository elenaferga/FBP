# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FBP'
copyright = '2024, Elena Fernandez'
author = 'Elena Fernandez'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.org/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'h5py': ('http://docs.h5py.org/en/latest/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}



intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

pygments_style = 'sphinx'

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
