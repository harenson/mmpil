#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classes.product_inventory import product, inventory
from classes.movie_store import movie, account, store

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


def test_movie():
    mov = movie.Movie(1, 'Scary Movie', 'comedy')
    assert str(mov) == 'Id: 1, Name: Scary Movie, Category: comedy'
    mov2 = movie.Movie(2, 'Scary Movie 2', 'comedy')
    assert str(mov2) == 'Id: 2, Name: Scary Movie 2, Category: comedy'


def test_account():
    acc1 = account.Account(1, 'john doe')
    assert str(acc1) == 'Id: 1, Fullname: John Doe'
    acc2 = account.Account(2, 'sheldon cooper')
    assert str(acc2) == 'Id: 2, Fullname: Sheldon Cooper'


def test_store():
    st = store.Store()
    mov = movie.Movie(1, 'Scary Movie', 'comedy')
    mov2 = movie.Movie(2, 'Scary Movie 2', 'comedy')
    acc1 = account.Account(1, 'jOhN dOe')
    acc2 = account.Account(2, 'sheldon cooper')
    st.add_movie(mov)
    st.add_movie(mov2)
    st.add_account(acc1)
    st.add_account(acc2)

    assert len(st.movies) == 2
    assert str(st.movies[0]) == 'Id: 1, Name: Scary Movie, Category: comedy'
    assert str(st.movies[1]) == 'Id: 2, Name: Scary Movie 2, Category: comedy'
    assert len(st.accounts) == 2
    assert str(st.accounts[0]) == 'Id: 1, Fullname: John Doe'
    assert str(st.accounts[1]) == 'Id: 2, Fullname: Sheldon Cooper'
    
    st.rent_movie(mov, acc1)
    st.rent_movie(mov2, acc1)
    assert len(st.rented_movies) == 2
    st.rent_movie(mov, acc2)
    st.rent_movie(mov2, acc2)
    assert len(st.rented_movies) == 4
