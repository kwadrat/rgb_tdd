#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
./tdd_suite.py test; red_green_bar.py $? $COLUMNS
'''

import sys
import unittest


class TestSimpleExample(unittest.TestCase):
    def test_simple_example(self):
        '''
        TestSimpleExample:
        '''
        self.assertEqual(0, 1)

fast_test_ls = [
    TestSimpleExample,
    ]


def add_all_fast(suite):
    for one_test in fast_test_ls:
        suite.addTest(unittest.makeSuite(one_test))


def perform_tests():
    suite = unittest.TestSuite()
    add_all_fast(suite)
    text_test_result = unittest.TextTestRunner().run(suite)
    result = not not (text_test_result.failures or text_test_result.errors)
    return result

if __name__ == '__main__':
    result = perform_tests()
    sys.exit(result)
