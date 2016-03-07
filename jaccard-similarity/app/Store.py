#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Product import Product
from Variables import Variables
from Client import Client
from random import randint
import numpy as np

const_vars = Variables()


class Store(object):

    def __init__(self, n_products, m_clients):
        self.n_products = n_products
        self.m_clients = m_clients
        self.store_matrix = None # Bidimensional matrix
        self.products = []
        self.clients = []

    # GETTERS
    def get_store_matrix(self):
        return self.store_matrix

    # METHODS
    def initialize_empty_matrix(self):
        row = len(self.clients)
        col = len(self.products)
        self.store_matrix = [[0 for c in range(col)] for r in range(row)]

    def generate_clients(self, m_clients):
        """
        Generates a list of clients and set to clients attribute on class.
        It takes into account the probabilities from "CLIENTS_TYPE"
        in order to generate the correct amount of clients for each type
        """
        left = 0
        offset = 0
        client_index = 0
        clients = [None] * m_clients

        for cat_name, cat_probability in const_vars.CLIENTS_PROBABILITIES().iteritems():

            clients_for_this_category = int(m_clients * cat_probability)
            left = offset
            offset = (left + clients_for_this_category)

            for i in range(0, clients_for_this_category):
                c = Client(name=str(client_index), favorite_category=cat_name)
                c.generate_information()
                clients[left+i] = c
                client_index += 1

        return clients

    def generate_products(self, n_products):
        """
        Generates a list of products with different categories.
        The number of products for each category is calculated taking into
        account the CATEGORIES probability global variable. Where defines what
        is the probability the system has clients for each category.
        """
        left = 0
        offset = 0
        product_index = 0
        products = [None] * n_products
        products_per_category = int(n_products / const_vars.TOTAL_CATEGORIES())

        for cat_name, cat_probability in const_vars.CATEGORIES().iteritems():

            left = offset
            products_for_this_category = products_per_category
            offset = (left + products_for_this_category)

            for i in range(0, products_for_this_category):
                p = Product(name=str(product_index), product_type=cat_name)
                products[left+i] = p
                product_index += 1

        return products

    def buy_client_products(self,
        n_products, m_client_products, categories_probability):
        """
        Generates a list of products bought by one client.
        Each element in the list can be 1 (the client has bought the product)
        or 0 (the client has not bought the product).
        When generating the list, it's creates a random "purchases".
        But if the client has bought all the products, don't make the random
        stuff and fill all the products for that range
        """

        left = 0
        offset = 0

        products = [0]*n_products
        s_categories = len(categories_probability)
        products_per_category = n_products / s_categories

        for probability in categories_probability:

            left = offset # Update left and right bounds
            offset = left + products_per_category

            added_products = 0
            total_products_to_add = int(probability * m_client_products)

            if total_products_to_add >= products_per_category:
                # The client has bought all the products for this category
                for i in range(0, products_per_category):
                    products[left] = 1
            else:
                # Fill random products for that client
                # At this point, we know the client has bought less products
                # that available products for that category. So we know this
                # while will eventually finish
                while added_products < total_products_to_add:
                    col_random = randint(left, offset - 1)
                    if products[col_random] == 0:
                        products[col_random] = 1
                        added_products += 1

        return products

    def generate_store_matrix(self, n_products, m_clients):
        """
        Returns a Bidimensional matrix where rows are clients
        and columns are products. The matrix relates for each client,
        the products he has bought

        Each element in the matrix can be 1 or 0.
        1= Client i has bought product j
        0= Client i has not bought product j
        """
        store_matrix = [] # Bidimensional matrix
        products = self.generate_products(n_products)
        clients = self.generate_clients(m_clients)

        for client in clients:
            m_client_products = client.get_purchases_number()
            categories_probability = client.get_categories_probability()

            client_products = self.buy_client_products(n_products,
                m_client_products, categories_probability)

            store_matrix.append(client_products)

        return store_matrix

    def init(self):
        """
        Creates products, clients and store_matrix.
        This function sets each attribute for the object after calculated
        """


        n_products = self.n_products
        m_clients = self.m_clients

        store_matrix = self.generate_store_matrix(n_products, m_clients)
        self.store_matrix = store_matrix

clients=10
products=100

s = Store(clients, products)
s.init()
