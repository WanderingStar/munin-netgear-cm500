#!/usr/bin/env python

from distutils.core import setup

setup(name='cm500',
      version='1.0',
      description='Python Distribution Utilities',
      author='Aneel Nazareth',
      author_email='github-python@account.loath.org',
      url='https://github.com/WanderingStar/munin-netgear-cm500.git',
      requires=['requests'],
      packages=['cm500'],
      scripts=['scripts/munin-netgear-cm500.py']
      )
