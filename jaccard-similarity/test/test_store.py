#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import numpy as np
from app.Store import Store

class TestStoreClass(unittest.TestCase):

    def setUp(self):
        self.store = Store()

    def test_store_initialize_matrix_to_all_ceroes(self):
        self.store.initialize_empty_matrix()

        store_matrix = self.store.get_store_matrix()
        matrix_full_of_zeroes = not np.any(store_matrix)

        self.assertEqual(matrix_full_of_zeroes, True)

    def test_store_generate_correct_clients_type(self):
        n_clients = 100

        clients_type = {
           "sport": 0.1,
           "science": 0.1,
           "film": 0.3,
           "informatic": 0.4,
           "politic": 0.1,
           "love": 0
        }

        for key, value in clients_type.iteritems():

            print key
            print value

    def test_store_add_all_the_products_the_client_wants_to_buy(self):
        s1 = Store()

        shop_products = 100
        client_products = 10 # client has bought 10 products
        category_probabilities = [0.2, 0.3, 0.2, 0.1, 0.2]

        list_products = s1.buy_client_products(
            shop_products, client_products, category_probabilities)

        # Test that previous method has filled the list correctly

        total_added_products = 0

        for col in range(0, shop_products):
            if list_products[col] == 1:
                total_added_products += 1

        self.assertEqual(client_products, total_added_products)

    def test_store_buy_all_products_for_each_category_correctly(self):
        s1 = Store()

        shop_products = 100
        client_products = 10 # client has bought 10 products
        probabilities = [0.2, 0.3, 0.2, 0.1, 0.2]
        n_categories = len(probabilities)

        list_products = s1.buy_client_products(
            shop_products, client_products, probabilities)

        # Check that the client has bought all the products for each category
        left = 0
        offset = 0
        products_per_category = shop_products / n_categories


        for probability in probabilities:
            left = offset
            offset = left + products_per_category
            category_products = int(client_products * probability)
            added_products = 0
            for i in range(0, products_per_category):
                if list_products[left+i] == 1:
                    added_products += 1
                # self.assertTrue(list_products[left+i] == 0)
            self.assertEqual(added_products, category_products)
