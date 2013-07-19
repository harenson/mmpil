#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reverse(string):
    """Returns the value of the "string" parameter, reversed"""
    string = unicode(str(string), 'utf-8') # for unicode characters
    return string[::-1] # iterates through the string, from the end to the start


if __name__ == '__main__':

    while True:
        try:
            user_text = 'What text do you want to reverse? [Ctrl+c to exit]: '
            word = raw_input(user_text)
            print reverse(word)
        except KeyboardInterrupt:
            print('\nGood bye')
            exit(0)
