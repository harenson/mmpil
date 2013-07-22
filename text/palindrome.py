#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def palindrome(input_text):
    """Check's if a given string is a palindrome string"""
    text = str(input_text).lower()
    text = re.sub('\W', '', text) # removes all alphanumerical characters

    if len(text) > 1:
        return text == text[::-1]
    else:
        return False



if __name__ == '__main__':
    while True:
        try:
            raw_input_text = 'Insert the text you want to check [Ctrl+c to exit]: '
            user_input = raw_input(raw_input_text)
            print palindrome(user_input)
        except KeyboardInterrupt:
            print('\n\nGood bye')
            break
