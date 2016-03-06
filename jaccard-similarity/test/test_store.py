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
