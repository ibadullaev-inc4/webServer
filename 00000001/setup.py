#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup
setup(
    name = 'srv',
    version='1.0',
    license='GNU General Public License v3',
    author='Nariman Ibadullaev',
    author_email='nibadullaev@inc4.net',
    description='Hello world application for Flask',
    packages=['srv'],
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
],
)