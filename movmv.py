#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : movmv.py
# Creation Date : 05-09-2013
# Last Modified : Thu 05 Sep 2013 07:33:03 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

import guessit

from sys import argv
from os import rename
from os import path


def main():
    fp = open(argv[1])
    for line in fp:
        name = line.strip()
        guess = guessit.guess_movie_info(name, info = ['filename'])
        #print guess.nice_string()
        while True:
            if path.isdir(name) == True:
                new_name = guess["title"]
            else:
                extension = name.split(".")[-1]
                new_name = "{0}.{1}".format(guess["title"], extension)

            ans = raw_input("Do you want me to rename '{0}' to '{1}'? (y/n) ".format(name, new_name))
            if ans == "y":
                rename(name, new_name)
            elif ans == "n":
                break
    fp.close()



if __name__=="__main__":
    main()

