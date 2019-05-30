#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages

import pyengine

setup(

    name='PyEngine-2D',

    version=pyengine.__version__,

    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="A lib to create 2D games",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    include_package_data=True,

    url='http://github.com/LavaPower/PyEngine',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: pygame",
        "Intended Audience :: Developers",
    ],
    install_requires=['pygame<2.0']

 
)