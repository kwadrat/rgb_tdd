#!/usr/bin/env python3

'''
Given:
1. status code: (0 - OK, other value - BAD)
2. terminal window width

shows red/green bar to visualize return code of previous command
'''

import sys

def main():
    if len(sys.argv) >= 2:
        code = sys.argv[1]
        if code == 'x':
            col_char = '3'
            cols_limit = 78
            code = '' # No code provided - only yellow bar
        else:
            if code == 'y':
                col_char = '3'
            else:
                value = int(code)
                if value:
                    col_char = '1'
                else:
                    col_char = '2'
            cols_limit = int(sys.argv[2])
        esc = chr(27)
        print (''.join((
            esc,
            '[4',
            col_char,
            'm',
            ' ' * (cols_limit - 2 - len(code)),
            code,
            esc,
            '[0m',
            )))
    else:
        print ('''
    Usage: %(prog_name)s status_code number_of_columns

    1. status code: 0 - OK (green color), other values - BAD (red color)
    2. number of columns: the width of text console
    ''' % dict(
            prog_name=sys.argv[0],
            ))
