#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from collections import Counter

def count_words(filename):
    try:
        f = open(filename) # open a file handler
        words = re.findall('\w+', f.read().lower()) # find all the words in the file and convert it to lowercase
        f.close() # close the file handler
        words_count = dict(Counter(words).most_common()) # counts the duplicated words and convert it to a dictionary
        words_total = 0
        for k, v in words_count.items():
            words_total += v
       
        words_count['total_words'] = words_total # add the total of all the words found in the file
        return words_count

    except:
        # the file couldn't be opened. Returns a message
        return('The file *%s* couldn\'t be opened.' % filename)


if __name__ == '__main__':

    filename = ''
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print count_words(filename)
    else:
        print('You have to give me a filepath with the filename at the end. '\
              'e.g: foo/bar/file.ext')
