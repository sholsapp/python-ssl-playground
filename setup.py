#!/usr/bin/env python

import os

from setuptools import setup

README = None
with open(os.path.abspath('README.md')) as fh:
  README = fh.read()

setup(
  name='python-ssl-playground',
  version='1.0.0',
  description=README,
  author='Stephen Holsapple',
  author_email='sholsapp@gmail.com',
  url='http://www.google.com',
  packages=['playground'],
  install_requires=[
    'Flask',
    'Flask-Script',
    'gunicorn',
    'cryptography',
    'certifi',
    'python-dateutil',
    'pyOpenSSL',
    'pytest',
    'py509',
    'tabulate',
  ],
)
