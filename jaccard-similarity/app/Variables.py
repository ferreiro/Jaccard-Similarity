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
        self.min_client_purchases = 10
        self.max_client_purchases = 20
        self.clients_probabilities = {
            # This must be 1 at total
            # Used when generating the number of clients
            "sport": 0.1,
            "science": 0.1,
            "film": 0.3,
            "informatic": 0.4,
            "politic": 0.1
        }
        self.screen_size = 80
        self.client_recurrency_factor = {
            'low': 1,
            'medium': 1,
            'high': 4
        }
        self.commun_probability = 10
        self.top_probability = 30



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

    def MIN_ALLOWED_PURCHASES(self):
        return self.min_client_purchases

    def MAX_ALLOWED_PURCHASES(self):
        return self.max_client_purchases

    def SCREEN_SIZE(self):
        return self.screen_size

    def CLIENT_RECURRENCY_FACTOR(self):
        # Constant Dictionary where the value (right element)
        # is the factor by we multiply the number of random purchases
        # make by the user when calculating the number of purchases
        return self.client_recurrency_factor

    def COMMUN_PROBABILITY(self):
        # Constant Dictionary where the value (right element)
        # is the factor by we multiply the number of random purchases
        # make by the user when calculating the number of purchases
        return self.commun_probability


    def TOP_PROBABILITY(self):
        # Constant Dictionary where the value (right element)
        # is the factor by we multiply the number of random purchases
        # make by the user when calculating the number of purchases
        return self.top_probability
