=====================
dict-recursive-update
=====================

.. image:: https://travis-ci.org/Maples7/dict-recursive-update.svg?branch=master
    :target: https://travis-ci.org/Maples7/dict-recursive-update

.. image:: https://img.shields.io/pypi/v/dict-recursive-update.svg
    :target: https://pypi.python.org/pypi/dict-recursive-update

A Python module who does recursive update work on 2 dicts.

Usage
=====

Installation
------------

.. code:: shell

    pip install dict-recursive-update


Examples
--------

.. code:: python

    >>> recursive_update({'a': {'b': 2}}, {'a': {'b': 3, 'd': 4}, 'e': 5})
    {'a': {'b': 3, 'd': 4}, 'e': 5}

    >>> recursive_update('a', 'b')
    Traceback (most recent call last):
        ...
    TypeError: Params of recursive_update should be dicts

    >>> recursive_update({'a': [1]}, {'a': [2], 'c': {'d': {'c': 3}}})
    {'a': [2], 'c': {'d': {'c': 3}}}

    >>> recursive_update({'a': {'c': 1, 'd': {}}, 'b': 4}, {'b': 5})
    {'a': {'c': 1, 'd': {}}, 'b': 5}

    >>> recursive_update({'a': {'c': 1, 'd': {}}, 'b': 4}, {'a': 2})
    {'a': 2, 'b': 4}


Why?
====

This is originally designed for merge multiple configurations in different running environment such as production or stage.

As a node.js developer, package `config <https://github.com/lorenwest/node-config>`_ and `lodash <https://github.com/lodash/lodash>`_ are very handy for me. This package is the base of `a python-version config package <https://github.com/Maples7/py-config>`_.

In a normal project, there is usually a copy of default configuration, but when we deploy it, some configurations differ from default ones like database address. So a handy configuration-loading package is supposed to load right configurations according to the running environment.

License
=======
`MIT <./LICENSE.txt>`_
