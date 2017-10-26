# -*- coding: utf-8 -*-
'''A Python module who does recursive update work on 2 dicts.

See:
https://github.com/Maples7/dict-recursive-update
'''
import codecs
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with codecs.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dict-recursive-update',
    version='1.0.0',
    description='A Python module who does recursive update work on 2 dicts.',
    long_description=long_description,
    url='https://github.com/Maples7/dict-recursive-update',
    author='Maples7',
    author_email='maples7@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='dict recursive update',
    packages=find_packages())
