#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.product_inventory import product, inventory

def test_product():
    monitor = product.Product(1, 'monitor', 250, 10)
    assert str(monitor) == 'Id: 1, Name: monitor, Price: $250usd, Quantity: 10'


def test_inventory():
    stock = inventory.Inventory()
    monitor = product.Product(1, 'monitor', 250, 10)
    keyboard = product.Product(2, 'keyboard', 15, 25)
    mouse = product.Product(3, 'mouse', 10, 25)
    # add the products to the inventory
    stock.add_to_stock(monitor)
    stock.add_to_stock(keyboard)
    stock.add_to_stock(mouse)
    assert stock.inventory_value() == (250 * 10) + (15 * 25) + (10 * 25)
    # duplicates the products within the inventory
    stock.add_to_stock(monitor)
    stock.add_to_stock(keyboard)
    stock.add_to_stock(mouse)
    assert stock.inventory_value() == ((250 * 10) + (15 * 25) + (10 * 25)) * 2
