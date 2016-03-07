#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Product import Product
from Variables import Variables
from Client import Client
from random import randint
import numpy as np
from operator import itemgetter

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
        clients = []

        for cat_name, cat_probability in const_vars.CLIENTS_PROBABILITIES().iteritems():

            clients_for_this_category = int(m_clients * cat_probability)
            left = offset
            offset = (left + clients_for_this_category)

            for i in range(0, clients_for_this_category):
                c = Client(name=str(client_index), favorite_category=cat_name)
                c.generate_information()
                clients.append(c)
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
        products = []
        products_per_category = int(n_products / const_vars.TOTAL_CATEGORIES())

        for cat_name, cat_probability in const_vars.CATEGORIES().iteritems():

            left = offset
            products_for_this_category = products_per_category
            offset = (left + products_for_this_category)

            for i in range(0, products_for_this_category):
                p = Product(name=str(product_index), product_type=cat_name)
                products.append(p)
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

    def generate_store_matrix(self, products, clients):
        """
        Returns a Bidimensional matrix where rows are clients
        and columns are products. The matrix relates for each client,
        the products he has bought

        Each element in the matrix can be 1 or 0.
        1= Client i has bought product j
        0= Client i has not bought product j
        """
        m_clients = len(clients)
        n_products = len(products)
        store_matrix = [] # Bidimensional matrix

        for client in clients:

            m_client_products = client.get_purchases_number()
            categories_probability = client.get_categories_probability()

            client_products = self.buy_client_products(n_products,
                m_client_products, categories_probability)

            store_matrix.append(client_products)

        return store_matrix

    def calculate_distance(self, store_matrix, rows, columnA, columnB):
        """
        Given a matrix, calculates the distante between 2 columns,
        applying the jaccard distance
        """
        distance = 0

        union = 0
        intersection = 0

        for i in range(0, rows):
            if store_matrix[i][columnA] == 1 and store_matrix[i][columnB] == 1:
                intersection += 1
            if store_matrix[i][columnA] == 1 or store_matrix[i][columnB] == 1:
                union += 1

        if union == intersection:
            return 0.0
        else:
            distance = intersection / float(union)
            return distance
    #
    # # Public method
    # def get_related_products(self):
    #     def calculate_related_products(store_matrix, rows, columns):
    #         distances = {
    #             # each key is the column index.
    #             # and the value associate with that key,
    #             # is the array of tuples (column, distanced) ordered from higher distance to lower.
    #         }
    #
    #         print "[ Calculating related products... ]"
    #
    #         for currentColumn in range(0, columns):
    #             A = currentColumn
    #             A_related_products = []
    #             for j in range(0, columns):
    #                 if A != j:
    #                     B = j
    #                     distanceAB = self.calculate_distance(store_matrix, rows, A, B)
    #                     column_distance = ( j, distanceAB )
    #                     A_related_products.append(column_distance)
    #             distances[currentColumn] = sorted(A_related_products,key=itemgetter(1), reverse=True)
    #
    #         print "[ Related products calculated. Thanks for your patience! ;) ]"
    #         return distances
    #
    #     store_matrix = self.store_matrix
    #     rows = self.m_clients
    #     cols = self.n_products
    #
    #     if store_matrix == None:
    #         return "Problems. The matrix is empty"
    #
    #     return calculate_related_products(store_matrix, rows, cols)
    #
    # def get_user_recommended_products(self, products_relation, user_index):
    #
    #     matrix = self.store_matrix
    #     rows = self.m_clients
    #     columns = self.n_products
    #
    #     debug = False
    #
    #     def get_pucharsed_product(user_index):
    #         purchased_products = []
    #         for c in range(0, columns):
    #             if matrix[user_index][c] == 1:
    #                 purchased_products.append(c) # add the column index
    #
    #         # print "\n\tPurchased products: " + str(purchased_products)
    #         return purchased_products
    #
    #     # calculate related products for the user
    #     purchased_list = get_pucharsed_product(user_index)
    #     total_purchases = len(purchased_list)
    #     products_to_recommend = {
    #         # "product_index" : "distance"
    #     }
    #
    #     for i in range(0, total_purchases):
    #         product_column = purchased_list[i]
    #         related_products_i = products_relation[product_column]
    #
    #         if debug: print "----------------"
    #         if debug: print "Related products"
    #         if debug: print "----------------"
    #
    #         if debug: print "\n"
    #         if debug: print related_products_i
    #         if debug: print "\n"
    #
    #         # traverse related products
    #         for product in related_products_i:
    #
    #             if debug: print "\n- Product: " + str(product)
    #
    #             index_product = product[0]
    #             product_distance_to_i = product[1]
    #
    #             if debug: print "\tIndex: " + str(index_product)
    #             if debug: print "\tDistance to i: " + str(product_distance_to_i)
    #
    #             if index_product in purchased_list: # get tuple first element (product index)
    #                 if debug: print "\t\t(YES) The user has purchased this object. So don't recommend it again"
    #                 pass
    #             else:
    #
    #                 if debug: print "\t\t(NOP) The user has not bought this product. we should recommend it"
    #                 if debug: print "\t\t     Check if the product is on the final recommendation list"
    #
    #                 if index_product in products_to_recommend:
    #                     if debug: print "\t\t\t(YES) The product is on the recommendation list."
    #                     if debug: print "\t\t\t      Check if the current product has greater distance the that previous element"
    #                     if product_distance_to_i > products_to_recommend[index_product]:
    #                         if debug: print "\t\t\t\t(YES) New distance is greater than previous one."
    #                         products_to_recommend[index_product] = product_distance_to_i
    #                     else:
    #                         if debug: print "\t\t\t\t(NOP) Previous distance is greater. So leave it."
    #                 else:
    #                     if debug: print "\t\t\t(NO) The product is NOT on the recommendation list. So add it"
    #                     products_to_recommend[index_product] = product_distance_to_i
    #             if debug: print "-------------------------"
    #         if debug: print products_to_recommend
    #         if debug: print "---"
    #
    #     convert_to_tuple = [(key, value) for key, value in products_to_recommend.iteritems()]
    #     convert_to_tuple.sort(key=itemgetter(1), reverse=True) # higher distance first on the tuple
    #
    #     return convert_to_tuple
    #
    # def get_all_users_recommended_products(self):
    #     users_recomendations = []
    #
    #     users = self.clients
    #     products = self.products
    #     n_users = len(users)
    #     related_products = self.get_related_products()
    #
    #     for user_id in range(0, n_users):
    #         recommended_products = self.get_user_recommended_products(
    #             related_products, user_id)
    #
    #         print users[user_id].to_str()
    #
    #         showed_product = 0
    #         for p in recommended_products:
    #             if showed_product > 10:
    #                 break
    #
    #             product_id = p[0]
    #             product_probability = p[1]
    #             print products[product_id].to_str()
    #             showed_product += 1
    #
    #         #print recommended_products
    #         users_recomendations.append(recommended_products)
    #
    #     return users_recomendations

    def init(self):
        """
        Creates products, clients and store_matrix.
        This function sets each attribute for the object after calculated
        """
        products = self.generate_products(self.n_products)
        clients = self.generate_clients(self.m_clients)
        store_matrix = self.generate_store_matrix(products, clients)

        self.products = products
        self.clients = clients
        self.store_matrix = store_matrix

clients=10
products=100

s = Store(products, clients)
s.init()
# s.get_all_users_recommended_products()
# print s.store_matrix
