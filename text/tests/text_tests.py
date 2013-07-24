#!/usr/bin/env python
# -*- coding: utf-8 -*-

from text.reverse_string import reverse # returns a reversed string
from text.count_vowels import count_vowels # count the vowels in a given text
from text.palindrome import palindrome # check if a given word is palindrome
from text.count_words import count_words # count the repetitions of every word in a given file

def test_reverse_string():
    assert reverse('reversed') == 'desrever'
    assert reverse('ßæ€') == unicode('€æß', 'utf-8') # unicode characters
    assert reverse('') == ''
    assert reverse(['hello']) == "]'olleh'[" # str() conversion
    assert reverse('12345') == '54321'
    assert reverse(12345) == '54321' # str() conversion


def test_count_vowels():
    assert count_vowels('hello world') == {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0, 'total': 3}
    assert count_vowels('héllo wórld') == {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0, 'total': 3}
    assert count_vowels('') == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total': 0}
    assert count_vowels('aeiouáéíóú') == {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2, 'total': 10}
    assert count_vowels('132') == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total': 0}


def test_palindrome():
    assert palindrome('racecar') == True
    assert palindrome('hello') == False
    assert palindrome('RaDaR') == True
    assert palindrome('Was it a car or a cat I saw?') == True
    assert palindrome('') == False


def test_count_words():
    pass
    # for this test to work, you have to execute nosetests from the parent folder of "tests" folder
    """
    response = {'a': 1, 'count': 1, 'file': 1, 'for': 1, 'this': 1, 'is': 1, 'total_words': 10, 'project': 1, 'words': 1, 'test': 1, 'the': 1}
    assert count_words('tests/count_words.txt') == response
    assert count_words('tests/empty_count_words.txt') == {'total_words': 0}
    response_string = 'The file *non_existing_file.txt* couldn\'t be opened.'
    assert count_words('non_existing_file.txt') == response_string
    """
