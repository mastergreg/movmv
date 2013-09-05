#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : movmv.py
# Creation Date : 05-09-2013
# Last Modified : Thu 05 Sep 2013 07:10:48 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import guessit

from sys import argv
from os import rename


def main():
    fp = open(argv[1])
    for line in fp:
        name = line.strip()
        guess = guessit.guess_movie_info(name, info = ['filename'])
        #print guess.nice_string()
        while True:
            ans = raw_input("Do you want me to move '{0}' to '{1}'? (y/n) ".format(name, guess["title"]))
            if ans == "y":
                rename(name, guess["title"])
                break
            elif ans == "n":
                break
    fp.close()



if __name__=="__main__":
    main()

