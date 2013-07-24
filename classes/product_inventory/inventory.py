#!/usr/bin/env python
# -*- coding: utf-8 -*-

import product

class Inventory(object):
    """Keeps track of various products"""

    def __init__(self):
        self.stock = [] # products list


    def add_to_stock(self, new_product):
        """Add a new Product to the inventory"""
        self.stock.append(new_product)


    def inventory_value(self):
        """Returns the sum up the inventory value"""
        total = 0
        n_items = len(self.stock) # number of items in the stock
        if n_items % 2 != 0: # check if n_items is odd
            self.add_to_stock(product.Product(0, 'generic', 0, 0)) # adds a generic item to make n_items even
            n_items += 1

        for k in range(0, n_items - 1, 2): # iterates the items in steps of 2
            total += self.stock[k] + self.stock[k + 1]
        
        self.stock.pop() # remove the generic element
        return int(total)
