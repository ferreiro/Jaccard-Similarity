# -*- coding: utf-8 -*-


class Variables(object):
    def __init__(self):
        self.n_products = int(10)
        self.m_clients = int(100)
        self.categories = {
            "sport": 0,
            "science": 1,
            "film": 2,
            "informatic": 3,
            "politic": 4
        }
        self.total_categories = len(self.categories)
        self.clients_probabilities = {
            # This must be 1 at total
            # Used when generating the number of clients
            "sport": 0.1,
            "science": 0.1,
            "film": 0.3,
            "informatic": 0.4,
            "politic": 0.1
        }

    def N_PRODUCTS(self):
        return self.n_products

    def M_CLIENTS(self):
        return self.m_clients

    def TOTAL_CATEGORIES(self):
        return self.total_categories

    def CATEGORIES(self):
        return self.categories

    def CLIENTS_PROBABILITIES(self):
        return self.clients_probabilities
