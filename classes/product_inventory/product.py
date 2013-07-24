#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Product(object):
    """Class for Products"""

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


    def __str__(self):
        """String representation of the object"""
        return 'Id: %d, Name: %s, Price: $%dusd, Quantity: %d' % \
                (self.product_id, self.name, self.price, self.quantity)


    def __add__(self, other):
        """Returns the sum of (self + other) product object"""
        return ((self.price * self.quantity) + (other.price * other.quantity))
