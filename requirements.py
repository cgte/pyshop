requires = [
    "pyramid >= 1.5",
    "SQLAlchemy",
    "pyramid_filterwarnings",
    "pyramid_jinja2",
    "pyramid_rpc",
    "pyramid_tm",
    "zope.sqlalchemy",
    "cryptacular",
    "requests",
    "docutils",
    "setuptools",  # compare package version
]

test_requires = ["pytest", "pyfakefs"]

extras_require = {
    "ldap": ["python-ldap",],
    "waitress": ["waitress",],
    "dev": ["waitress", "pyramid_debugtoolbar",],
    "shell": ["IPython",],
    "docs": ["sphinx", "sphinx_rtd_theme"],
    "wheelify": ["wheel",],  # build wheels from source on the proxy
    "test": test_requires,
}



