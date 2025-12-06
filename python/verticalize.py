#!/usr/bin/env python3
"""
Verticalizes text from stdin

   $ echo -n "こんにちは、世界。" | ./verticalize.py --width 2
   、こ
   世ん
   界に
   。ち
   　は

   $ echo -n "こんにちは、世界。" | ./verticalize.py --width 3
   世ちこ
   界はん
   。、に
"""

import argparse
import math
import sys

parser = argparse.ArgumentParser(
                    prog='Verticalize',
                    description='Verticalizes text from stdin')
parser.add_argument('-w', '--width', type=int, default=3)

def verticalize(s: str, width: int) -> str:
    """
    Verticalizes a string such that the output has `ceil(len(s)/width)` lines
    each with `width` characters.
    """

    # TODO(janreggie): Replace quotations with a mapping.

    height = math.ceil(len(s)/width)
    vertical_words = [s[height*i:height*(i+1)].ljust(height, '\u3000')
                      for i in range(0, width)]
    vertical_words.reverse()

    rows = [''.join(word[i] for word in vertical_words) for i in range(height)]
    return '\n'.join(rows)


def main():
    """Main program"""
    args = parser.parse_args()
    for line in sys.stdin:
        print(verticalize(line.strip(), args.width))


if __name__ == '__main__':
    main()
