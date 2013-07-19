#!/usr/bin/env python
# -*- coding: utf-8 -*-

from text.reverse_string import reverse # returns a reversed string

def test_reverse_string():
    assert reverse('reversed') == 'desrever'
    assert reverse('ßæ€') == unicode('€æß', 'utf-8') # unicode characters
    assert reverse('') == ''
    assert reverse(['hello']) == "]'olleh'[" # str() conversion
    assert reverse('12345') == '54321'
    assert reverse(12345) == '54321' # str() conversion
