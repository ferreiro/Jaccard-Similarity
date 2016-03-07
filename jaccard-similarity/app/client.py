# -*- coding: utf-8 -*-

import random
from random import randint
from Variables import Variables
const_vars = Variables()


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

    def to_str(self):
        client_str = "\n"
        client_str += "-" * const_vars.SCREEN_SIZE()
        client_str += "\n\tName: " + self.name
        client_str += "\n\tRecurrency: " + self.recurrency
        client_str += "\n\tProbabilities: " + str(self.categories_probability)
        client_str += "\n\tTotal purchases: " + str(self.purchases_number)
        client_str += "\n\tFavorite Category: " + str(self.favorite_category)

        # Print the rest of categories from most probability to bottom
        for i in range(0, const_vars.TOTAL_CATEGORIES()):
            client_str += "\n\tGet probability for this category"

        return client_str

    def get_recurrency_num(self, key, recurrency_dict):
        if key in recurrency_dict:
            return recurrency_dict[key]
        else:
            return 0

    def set_random_recurrency(self):
        self.recurrency = random.choice(const_vars.CLIENT_RECURRENCY_FACTOR().keys())

    def set_random_purchases_number(self, recurrency_key):
        random_purchases_num = randint(
            const_vars.MIN_ALLOWED_PURCHASES(),
            const_vars.MAX_ALLOWED_PURCHASES())

        increase_purchases_by_factor = self.get_recurrency_num(
            recurrency_key, const_vars.CLIENT_RECURRENCY_FACTOR())

        total_purchases = random_purchases_num * increase_purchases_by_factor

        if total_purchases >= const_vars.MAX_ALLOWED_PURCHASES():
            total_purchases = const_vars.MAX_ALLOWED_PURCHASES()

        self.purchases_number = total_purchases

    def set_random_categories_probability(self, favourite_category, categories):
        """
        Calculates a list of probabilities and set to the current user.
        Each index on the list, represents the probability that the user has
        to buy products from that particular category.

        When the parameter "favourite_category" is provided,
        the user will increase the probability for that particular category
        by a constant factor "const_vars.TOP_PROBABILITY()"
        """
        total = const_vars.COMMUN_PROBABILITY() * const_vars.TOTAL_CATEGORIES()
        categories_probability = [0] * const_vars.TOTAL_CATEGORIES()

        for i in range(0, const_vars.TOTAL_CATEGORIES()):
            categories_probability[i] = const_vars.COMMUN_PROBABILITY()

        if favourite_category in categories:
            # When Client index is valid, add extra value to that category
            top_cat_index = categories[favourite_category]
            total += const_vars.TOP_PROBABILITY()
            categories_probability[top_cat_index] += const_vars.TOP_PROBABILITY()

        # Converting values into probabilities
        for i in range(0, const_vars.TOTAL_CATEGORIES()):
            categories_probability[i] /= float(total)

        self.categories_probability = categories_probability
        # return products

    def generate_random_information(self, recurrency_key, favourite_category):

        self.set_random_recurrency()

        self.set_random_purchases_number(
            recurrency_key)

        self.set_random_categories_probability(
            favourite_category,
            const_vars.CATEGORIES())

    def generate_information(self):
        recurrency_key = self.recurrency
        favourite_category = self.favorite_category
        self.generate_random_information(recurrency_key, favourite_category)


def __test():
    p1 = Client('Jorge', 'low', 'love')
    p1.generate_information()
    info = p1.to_str()

    print info

    p2 = Client('Jorge', 'high', 'love')
    p2.generate_information()
    info = p2.to_str()

    print info

    p2 = Client('Jorge', 'medium', 'sport')
    p2.generate_information()
    info = p2.to_str()

    print info
