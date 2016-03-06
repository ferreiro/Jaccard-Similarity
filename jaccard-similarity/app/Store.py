#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Product import Product
from Variables import Variables
from Client import Client

const_vars = Variables()

class Store(object):

    def __init__(
        self,
        products=([None] * const_vars.N_PRODUCTS()),
        clients=([None] * const_vars.M_CLIENTS())
    ):
        self.products = products
        self.clients = clients
        self.store_matrix = None

    # GETTERS
    def get_store_matrix(self):
        return self.store_matrix

    # METHODS
    def initialize_empty_matrix(self):
        row = len(self.clients)
        col = len(self.products)
        self.store_matrix = [[0 for c in range(col)] for r in range(row)]

    def generate_clients(self):
        """
        Generates a list of clients and set to clients attribute on class.
        It takes into account the probabilities from "CLIENTS_TYPE"
        in order to generate the correct amount of clients for each type
        """
        left = 0
        offset = 0
        client_index = 0
        clients = [None] * const_vars.M_CLIENTS()

        for cat_name, cat_probability in const_vars.CLIENTS_PROBABILITIES().iteritems():

            clients_for_this_category = int(const_vars.M_CLIENTS() * cat_probability)
            left = offset
            offset = (left + clients_for_this_category)

            for i in range(0, clients_for_this_category):
                c = Client(name=str(client_index), favorite_category=cat_name)
                c.generate_information()
                clients[left+i] = c
                client_index += 1

        self.clients = clients

    def generate_products(self):
        left = 0
        offset = 0
        product_index = 0
        products = [None] * const_vars.N_PRODUCTS()
        products_per_category = int(const_vars.N_PRODUCTS() / const_vars.TOTAL_CATEGORIES())

        for cat_name, cat_probability in const_vars.CATEGORIES().iteritems():

            products_for_this_category = products_per_category
            left = offset
            offset = (left + products_for_this_category)

            for i in range(0, products_for_this_category):
                p = Product(name=str(product_index), product_type=cat_name)
                products[left+i] = p
                product_index += 1

        self.products = products

    def fill_store_matrix(self):
        """
        When we have already the products and the clients,
        We can start filling the matrix content.
        So for each client, we have to generate products
        inside each category, depending on the probabilities he has on
        his profile
        """
        pass

s = Store()
s.initialize_empty_matrix()
s.generate_clients()
s.generate_products()
print s.clients
print s.products
