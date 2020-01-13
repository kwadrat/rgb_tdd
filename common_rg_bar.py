#!/usr/bin/env python3

'''
Given:
1. status code: (0 - OK, other value - BAD)
2. terminal window width
3. (optional) Text to display (without color)

shows red/green bar to visualize return code of previous command
'''

import sys

esc = chr(27)

def unicolor_emit(start_text, col_char, cols_limit, code):
    print(''.join((
        start_text,
        esc,
        '[4',
        col_char,
        'm',
        ' ' * (cols_limit - 2 - len(code) - len(start_text)),
        code,
        esc,
        '[0m',
        )))


def dual_tape_emit(cols_limit):
    red = [esc, '[4', '1', 'm', ' ']
    white = [esc, '[4', '7', 'm', ' ']
    end = [esc, '[0m']

    all_text = (red + white) * (cols_limit // 2)
    if cols_limit % 2:
        all_text.extend(red)
    all_text.extend(end)
    print(''.join(all_text))


def main():
    if len(sys.argv) >= 2:
        code = sys.argv[1]
        if code == 'x':
            col_char = '3'
            cols_limit = 78
            code = '' # No code provided - only yellow bar
        elif code == 't':
            if len(sys.argv) >= 3:
                cols_limit = int(sys.argv[2]) - 2
            else:
                cols_limit = 78
            dual_tape_emit(cols_limit)
            sys.exit(0)
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
        if len(sys.argv) >= 4:
            start_text = sys.argv[3] + ' '
        else:
            start_text = ''
        unicolor_emit(start_text, col_char, cols_limit, code)
    else:
        print('''
    Usage: %(prog_name)s status_code number_of_columns

    1. status code: 0 - OK (green color), other values - BAD (red color)
    2. number of columns: the width of text console
    3. (optional) Text to display
    ''' % dict(
            prog_name=sys.argv[0],
            ))
