#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Template file for testing functions and classes
./simple_tdd_template.py test; red_green_bar.py $? $COLUMNS
'''

import sys
import unittest


class TestSomething(unittest.TestCase):
    '''
    General class for testing
    '''
    def test_something(self):
        '''
        TestSomething:
        '''
        self.assertEqual(0, 1)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
