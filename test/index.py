#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from dict_recursive_update import recursive_update


class Test(unittest.TestCase):
    def test_all(self):
        self.assertEqual(
            recursive_update({
                'a': {
                    'b': 2
                }
            }, {'a': {
                'b': 3,
                'd': 4
            },
                'e': 5}), {'a': {
                    'b': 3,
                    'd': 4
                },
                           'e': 5})

        self.assertEqual(
            recursive_update({
                'a': [1]
            }, {'a': [2],
                'c': {
                    'd': {
                        'c': 3
                    }
                }}), {'a': [2],
                      'c': {
                          'd': {
                              'c': 3
                          }
                      }})

        self.assertEqual(
            recursive_update({
                'a': {
                    'c': 1,
                    'd': {}
                },
                'b': 4
            }, {'b': 5}), {'a': {
                'c': 1,
                'd': {}
            },
                           'b': 5})
        self.assertEqual(
            recursive_update({
                'a': {
                    'c': 1,
                    'd': {}
                },
                'b': 4
            }, {'a': 2}), {'a': 2,
                           'b': 4})


if __name__ == '__main__':
    unittest.main()
