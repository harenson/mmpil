#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Movie(object):
    """Class for movies"""

    def __init__(self, movie_id, name, category):
        self.movie_id = movie_id
        self.name = name
        self.category = category


    def __str__(self):
        return 'Id: %d, Name: %s, Category: %s' % (self.movie_id,
                                                   self.name,
                                                   self.category)
