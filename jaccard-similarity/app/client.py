# -*- coding: utf-8 -*-

from random import randint

N_CATEGORIES = 5
BASE_PROBABILITY = 10
TOP_PROBABILITY = 30
MAX_BOUGHT_PRODUCTS = 10

# Constant Dictionary where the value (right element)
# is the factor by we multiply the number of random purchases
# make by the user when calculating the number of purchases
CLIENT_RECURRENCY_FACTOR = {
    'low': 1,
    'medium': 2,
    'high': 3
}


class Client(object):

    def __init__(self, name='', recurrency='low', fav_category=''):
        self.name = name
        self.purchases_number = 0  # Number of sold products
        self.fav_category = fav_category
        self.recurrency = recurrency

    # GETTERS
    def get_purchases_number(self):
        return self.purchases_number

    # METHODS
    def get_recurrency_num(self, key, recurrency_dict):
        if key in recurrency_dict:
            return recurrency_dict[key]
        else:
            return 0

    def set_random_purchases_number(self, recurrency_key):
        random_purchases_num = randint(1, MAX_BOUGHT_PRODUCTS-1)
        increase_purchases_by_factor = self.get_recurrency_num(
            recurrency_key, CLIENT_RECURRENCY_FACTOR)

        total_purchases = random_purchases_num * increase_purchases_by_factor

        self.purchases_number = total_purchases

    def buy_products(self, client_fav_category):
        """
        Return a list containing probabilities
        that the client buy products from each category.
        When 'fav_category' is provided, we
        assign 3x more probabilities to that category
        """
        total = BASE_PROBABILITY * N_CATEGORIES
        products = [0] * N_CATEGORIES
        top_cat_index = client_fav_category

        for i in range(0, N_CATEGORIES):
            products[i] = BASE_PROBABILITY

        if (top_cat_index >= 0 and top_cat_index <= len(products)-1 and
                isinstance(top_cat_index, int)):
            # When Client index is valid, add extra value to that category
            total += TOP_PROBABILITY
            products[top_cat_index] += TOP_PROBABILITY

        # Converting values into probabilities
        for i in range(0, N_CATEGORIES):
            products[i] /= float(total)

        return products

    def generate_random_information(self, recurrency, fav_category):
        pass

    # def is_valid_recurrency(self, recurrency, valid_recurrencies_dict):
    #     return recurrency in valid_recurrencies_dict
