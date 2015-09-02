# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    
    HTTP Proxy Server in Python with explicit WebSocket support.

    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.

    Added WebSocket support to modify and change WebSocket messages on Summer 2015.
    The original source code may be found on:

    https://github.com/abhinavsingh/proxy.py
"""
from setuptools import setup
import proxy

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: Microsoft',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: Proxy Servers',
    'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
]

setup(
    name                = 'proxy-websockets',
    version             = proxy.__version__,
    description         = proxy.__description__,
    long_description    = open('README.md').read().strip(),
    author              = proxy.__author__,
    author_email        = proxy.__author_email__,
    url                 = proxy.__homepage__,
    license             = proxy.__license__,
    py_modules          = ['proxy'],
    scripts             = ['proxy.py'],
    install_requires    = [],
    classifiers         = classifiers
)
