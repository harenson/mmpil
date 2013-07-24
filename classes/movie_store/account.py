#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Account(object):
    """Class for Accounts"""

    def __init__(self, account_id, fullname):
        self.account_id = account_id
        self.fullname = fullname


    def __str__(self):
        return 'Id: %d, Fullname: %s' % (self.account_id, self.fullname.title())
