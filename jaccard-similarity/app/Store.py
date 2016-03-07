#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Product import Product
from Variables import Variables
from Client import Client
from random import randint

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

            left = offset
            products_for_this_category = products_per_category
            offset = (left + products_for_this_category)

            for i in range(0, products_for_this_category):
                p = Product(name=str(product_index), product_type=cat_name)
                products[left+i] = p
                product_index += 1

        self.products = products


    def buy_client_products(self,
        n_products, m_bought_products, categories_probability):

        products = [0]*n_products
        s_categories = len(categories_probability)
        products_per_category = n_products / s_categories
        left = 0
        offset = 0

        for probability in categories_probability:
            # Update left and right bounds
            left = offset
            offset = left + products_per_category

            added_products = 0
            total_products_to_add = int(probability * m_bought_products)

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
                    # print "\t" + str(added_products)
                    col_random = randint(left, offset - 1)
                    if products[col_random] == 0:
                        products[col_random] = 1
                        # print "\t bought?"+ str(products[col_random])
                        added_products += 1
        print products
        return products
    #
    # def buy_client_products(
    #     self, shop_products, client_products, category_probabilities):
    #     """
    #     Returns a binary list (1=client has bought the product and 0=non bought product)
    #     that is the row for that client and the columns size is the total amount of products
    #     we have in the store
    #     """
    #     left = 0
    #     offset = 0
    #     products_list = [0] * shop_products
    #     n_categories = len(category_probabilities)
    #     products_per_category = shop_products / n_categories
    #     max_attempts = 30 # Timeout that prevents infinite loops when adding random purchased fails
    #
    #     for i in range(0, n_categories):
    #
    #
    #
    #         attempts = 0
    #         left = offset
    #         offset = left + products_per_category
    #         category_products = int(client_products * category_probabilities[i])
    #
    #         if category_products >= products_per_category:
    #             # Buy all the products for this category
    #             for j in range(0, category_products):
    #                 products_list[left + j] = 1 # buy the products
    #
    #         else:#Fill random products
    #             added_products = 0
    #             print added_products
    #             while added_products < category_products:
    #                 rand_product = randint(left, offset-1)
    #                 print "Rand: " + str(rand_product)
    #                 print "Value?: " + str(products_list[rand_product])
    #                 if products_list[rand_product] == 0:
    #                     products_list[rand_product] = 1
    #                     added_products += 1
    #                     print "Set!"
    #                 print "---"
    #             print added_products
    #
    #     return products_list
    #
    # def buy_client_products(self, total_products, client_row, clients_products, client_probabilities):
    #     matrix_full_of_zeroes = [
    #         [0 for c in range(num_of_products)] for r in range(num_of_clients)]
    #
    #

    #
    # def buy_client_products(self, total_products, client_row, clients_products, client_probabilities):
    #     """
    #     Buys products for the client (given his index in the matrix)
    #     taking into account the probabilities that client has to buy
    #     products for each category.
    #
    #     This method sets the private attribute store_matrix
    #     """
    #     products = self.products
    #     store_matrix = self.store_matrix
    #
    #     left = 0
    #     offset = 0
    #     max_allowed_attemps = len(products) # Prevent inifinite loops while trying to fill the matrix
    #     products_per_category = len(products) / const_vars.TOTAL_CATEGORIES()
    #
    #     print
    #     print "Initial matrix " +  str(store_matrix)
    #     print "Probabilities " + str(client_probabilities)
    #
    #     # Traverse all the client probabilities and fill the products
    #     # for each category, according user bought products
    #
    #     for p in client_probabilities:
    #         i = 0
    #         attempts = 0
    #         left = offset
    #         offset = left + products_per_category
    #         total_category_products = int(p * clients_products)
    #
    #         print "Left " + str(left)
    #         print "Offset " + str(offset)
    #         print "Products for this category: " + str(total_category_products)
    #
    #         while i < total_category_products and attempts < max_allowed_attemps:
    #             random_index = randint(left, offset-1)
    #             if store_matrix[client_row][random_index] == 0:
    #                 store_matrix[client_row][random_index] = 1
    #                 print "\tYoo"
    #                 i += 1 # we have added one product
    #             attempts += 1
    #
    #
    #     print store_matrix
    #     self.store_matrix = store_matrix

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
