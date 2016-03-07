#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import numpy as np
from app.Store import Store

class TestStoreClass(unittest.TestCase):

    def setUp(self):
        n_products = 100
        m_clients = 10
        self.store = Store(n_products, m_clients)
    # TODO
    # def test_store_creates_list_of_clients(self):
    #     self.assertEqual(2, 0, "TODO: Creates a list of clients")
    #
    # TODO
    # def test_store_creates_list_of_products(self):
    #     self.assertEqual(2, 0, "TODO: Creates a list of products")

    def test_store_initialize_matrix_to_all_ceroes(self):
        self.store.initialize_empty_matrix()

        store_matrix = self.store.get_store_matrix()
        matrix_full_of_zeroes = not np.any(store_matrix)

        self.assertEqual(matrix_full_of_zeroes, True)

    def test_store_add_all_the_products_the_client_wants_to_buy(self):
        n_products = 100
        m_clients = 10

        s1 = Store(n_products, m_clients)

        client_products = 10 # client has bought 10 products
        category_probabilities = [0.2, 0.3, 0.2, 0.1, 0.2]

        list_products = s1.buy_client_products(
            n_products, client_products, category_probabilities)

        # Test that previous method has filled the list correctly

        total_added_products = 0

        for col in range(0, n_products):
            if list_products[col] == 1:
                total_added_products += 1

        self.assertEqual(client_products, total_added_products)

    def test_store_fill_all_products_for_each_category_correctly(self):
        n_products = 100
        m_clients = 10
        s1 = Store(n_products, m_clients)

        client_products = 10 # client has bought 10 products
        probabilities = [0.2, 0.3, 0.2, 0.1, 0.2]
        n_categories = len(probabilities)

        list_products = s1.buy_client_products(
            n_products, client_products, probabilities)

        # Check that the client has bought all the products for each category
        left = 0
        offset = 0
        products_per_category = n_products / n_categories


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

    def test_store_initialize_matrix(self):
        """
        Given a list of clients and products, generates a matrix
        where each row contains is a list of ceroes and one's
        of bought products by each client
        """
        n_products = 100
        m_clients = 10
        s1 = Store(n_products, m_clients)
        # clients_type = [0.2, 0.2, 0.2, 0.2, 0.2] # All the clients has the same type.

        products = s1.generate_products(n_products)
        clients = s1.generate_clients(m_clients)

        store_matrix = s1.generate_store_matrix(products, clients) #, clients_type)

        # Test matrix has changed (and filled)
        self.assertNotEqual(store_matrix, None)

        # Test dimensions of the new matrix
        dimensions = np.shape(store_matrix)
        aux_row = dimensions[0]
        aux_col = dimensions[1]

        self.assertEqual(aux_row, m_clients)
        self.assertEqual(aux_col, n_products)

        # Check that for each client, we have a list

        for row in store_matrix:
            self.assertTrue(len(row) > 0 and isinstance(row, list))
    #
    # def test_store_calculate_distance(self):
    #     n_products = 2
    #     m_clients = 4
    #     s1 = Store(n_products, m_clients)
    #
    #     columnA = [0, 1, 0, 1] # Product Column
    #     columnB = [1, 0, 0, 1] # Product Column
    #
    #     union = 3
    #     intersection = 1
    #
    #     distance_result = intersection / float(union)
    #     distance = s1.calculate_distance(columnA, columnB)
    #
    #     self.assertEqual(distance, distance_result)
    #
    # def test_store_calculate_related_products(self):
    #     n_products = 2
    #     m_clients = 4
    #     s1 = Store(n_products, m_clients)
    #     related = []
    #
    #     product1 = [1, 1, 1, 1]
    #     product2 = [0, 0, 0, 1]
    #     product3 = [1, 1, 1, 1]
    #
    #     product_column = 0
    #
    #     store_matrix = [ product1, product2, product3 ]
    #     related = s1.get_related_products(product_column, store_matrix)
    #
    #     max_product = max(related)
    #     assertEqual()
