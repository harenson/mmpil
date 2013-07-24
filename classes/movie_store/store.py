#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Store(object):
    """Class to manage Movies and Accounts"""

    def __init__(self):
        self.movies = [] # movies list
        self.accounts = [] # accounts list
        self.rental_fee = 100 # fee to pay for the movie rental
        self.__overdue_fee = 20 # fee to pay for delay in returning the movie
        self.__rented_movies = []


    @property
    def overdue_fee(self):
        return self.__overdue_fee


    @property
    def rented_movies(self):
        return self.__rented_movies


    def add_movie(self, movie):
        """Appends a movie to the movies list"""
        self.movies.append(movie)


    def add_account(self, account):
        """Appends an account to the accounts list"""
        self.accounts.append(account)


    def rent_movie(self, movie, account):
        self.__rented_movies.append([movie, account])
