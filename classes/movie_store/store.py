#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time, strftime, gmtime

class Store(object):
    """Class to manage Movies and Accounts"""

    def __init__(self):
        self.movies = [] # movies list
        self.accounts = [] # accounts list
        self.__rented_movies = {}


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
        """Register rented movies. It classify the rented movies by account"""
        if  not self.__rented_movies.has_key(account): # verifies if the account already has rented movies
            self.__rented_movies[account] = [] # else create a new empty array for the account to hold the rented movies

        actual_time = float(time()) # gets the actual time in seconds
        rend_date = strftime('%Y-%m-%d', gmtime(actual_time)) # formats the actual time value to YYYY-MM-DD
        due_to_return = strftime('%Y-%m-%d', gmtime(actual_time + 86400)) # adds one day (86400 seconds) to the actual time
        self.__rented_movies[account].append(dict(mov=movie,
                                                  rend_date=rend_date,
                                                  due_to_return=due_to_return))


    def overdue_accounts(self):
        """Return the list of accounts with overdue movie rental"""
        overdue_accounts = {}

        today = strftime('%Y-%m-%d', gmtime(time()))

        for account in self.__rented_movies:
            for movie in self.__rented_movies[account]:
                if str(today) > str(movie['due_to_return']):
                    if not overdue_accounts.has_key(account):
                        overdue_accounts[account] = []

                    overdue_accounts[account].append(movie)

        return overdue_accounts
