# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

AUTHOR = u'Markus Törnqvist'
AUTHOR_EMAIL = 'mjt@skyhood.com'
URL = 'https://github.com/mjtorn/django-jsoneditor'

import jsoneditor

from distutils.core import setup

description = 'Django JSON editor'

try:
    with open('README.rst') as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name = 'django-jsoneditor',
    version = jsoneditor.__version__,
    description = description,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    long_description = long_description,
    packages = ['jsoneditor'],
)

# EOF
