#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
  name = 'tespeed',

  # Since this package is simple, just reference the .py file
  # directly instead of specifying a particular package
  py_modules = ['tespeed.tespeed'],

  # TODO: Make this dynamically retrieved from a source file for easier maintenance
  version = '1.1.0',
  description = 'Terminal network speed test that uses servers from Speedtest.net. It uses nearest test server but can also use one manually specified by the user',

  license = 'MIT',

  author = 'Janis Jansons',
  author_email = 'janis.jansons@janhouse.lv',
  url = 'https://github.com/gauthamchandra/tespeed',

  download_url = 'https://github.com/Janhouse/tespeed/tarball/1.1',
  keywords = 'speedtest.net network speed',

  # dependencies
  # TODO: Add upper and lower bound versions of compatibility so bleeding edge dependency doesn't break
  #       the app
  install_requires = ['lxml', 'argparse'],

  entry_points = {
    'console_scripts': [
        'tespeed=tespeed.tespeed:init'
    ]
  },

  # Full list here: https://pypi.python.org/pypi?%3Aaction=list_classifiers
  classifiers = [
    # Lifecycle of this version
    'Development Status :: 5 - Production/Stable',

    # The license the software is under
    'License :: OSI Approved :: MIT License',

    # What category and audience it may fall under
    'Programming Language :: Python',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'Topic :: Utilities',
    'Intended Audience :: System Administrators',

    # Supported versions
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 2 :: Only',
  ],
)
