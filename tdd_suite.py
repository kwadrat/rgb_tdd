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


slow_test_ls = [
    TestSimpleExample,
    ]


def add_all_fast(suite):
    for one_test in fast_test_ls:
        suite.addTest(unittest.makeSuite(one_test))


def add_all_slow(suite):
    for one_test in slow_test_ls:
        suite.addTest(unittest.makeSuite(one_test))


def summary_status(suite):
    text_test_result = unittest.TextTestRunner().run(suite)
    return not not (text_test_result.failures or text_test_result.errors)


def perform_tests():
    suite = unittest.TestSuite()
    add_all_fast(suite)
    return summary_status(suite)


def perform_slow_tests():
    suite = unittest.TestSuite()
    add_all_fast(suite)
    add_all_slow(suite)
    return summary_status(suite)


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'slowtest':
        result = perform_slow_tests()
    else:
        result = perform_tests()
    sys.exit(result)
