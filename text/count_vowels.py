#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def count_vowels(input_text):
    """Returns the number of occurrences by vowel in a text and the
       total of all of them"""
    text = str(input_text)
    # total vowels one by one and the total of all vowels
    total_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total': 0}
    # will be used to replace vowels with spanish acent e.g: canción
    to_replace = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}

    # replace vowels with spanish acent
    for k, v in to_replace.items():
        text = text.replace(k, v)

    # find the vowels in the input text
    vowels = re.findall('[aeiou]', text)

    # count vowels one by one and the total
    for vowel in vowels:
        total_vowels[vowel] += 1
        total_vowels['total'] += 1

    return total_vowels



if __name__ == '__main__':

    while True:
        try:
            user_input = raw_input('Please, enter some text (Ctrl+C to exit): ')
            print count_vowels(user_input)
        except KeyboardInterrupt:
            print '\n\nGood bye'
            break
