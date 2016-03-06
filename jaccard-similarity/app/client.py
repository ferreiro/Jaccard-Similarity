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

    def __init__(self, name='', recurrency='low', favorite_category=''):
        self.name = name
        self.categories_probability = []  # Each index is for each product type
        self.purchases_number = 0  # Number of sold products
        self.favorite_category = favorite_category
        self.recurrency = recurrency

    # GETTERS

    def get_purchases_number(self):
        return self.purchases_number

    def get_recurrency(self):
        return self.recurrency

    def get_categories_probability(self):
        return self.categories_probability

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

    def set_random_categories_probability(self, favourite_category, categories):
        """
        Calculates a list of probabilities and set to the current user.
        Each index on the list, represents the probability that the user has
        to buy products from that particular category.

        When the parameter "favourite_category" is provided,
        the user will increase the probability for that particular category
        by a constant factor "TOP_PROBABILITY"
        """
        total = BASE_PROBABILITY * N_CATEGORIES
        categories = [0] * N_CATEGORIES

        for i in range(0, N_CATEGORIES):
            categories[i] = BASE_PROBABILITY

        if favourite_category in categories:
            # When Client index is valid, add extra value to that category
            top_cat_index = categories[favourite_category]
            total += TOP_PROBABILITY
            categories[top_cat_index] += TOP_PROBABILITY

        # Converting values into probabilities
        for i in range(0, N_CATEGORIES):
            categories[i] /= float(total)

        self.categories_probability = categories
        # return products

    def generate_random_information(self, recurrency_key, favourite_category):

        self.set_random_purchases_number(recurrency_key)
        self.set_random_categories_probability(favourite_category)
