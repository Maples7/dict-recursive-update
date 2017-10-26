#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A recursive version of Python dict#update

>>> recursive_update({'a': {'b': 2}}, {'a': {'b': 3, 'd': 4}, 'e': 5})
{'a': {'b': 3, 'd': 4}, 'e': 5}
'''


def recursive_update(default, custom):
    '''Return a dict merged from default and custom

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
    '''
    if not isinstance(default, dict) or not isinstance(custom, dict):
        raise TypeError('Params of recursive_update should be dicts')

    for key in custom:
        if isinstance(custom[key], dict) and isinstance(
                default.get(key), dict):
            default[key] = recursive_update(default[key], custom[key])
        else:
            default[key] = custom[key]

    return default


if __name__ == '__main__':
    import doctest
    doctest.testmod()
