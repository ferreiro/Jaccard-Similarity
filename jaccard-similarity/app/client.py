# -*- coding: utf-8 -*-

import random
from random import choice, randint
from Category import Category

category = Category()
AVAILABLE_CATEGORIES = category.CATEGORIES()
N_CATEGORIES = category.N_CATEGORIES()

MAX_BOUGHT_PRODUCTS = 10
BASE_PROBABILITY = 10
TOP_PROBABILITY = 30
SCREEN_SIZE = 80

# Constant Dictionary where the value (right element)
# is the factor by we multiply the number of random purchases
# make by the user when calculating the number of purchases
CLIENT_RECURRENCY_FACTOR = {
    'low': 1,
    'medium': 2,
    'high': 4
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

    def to_str(self):
        client_str = "\n"
        client_str += "-" * SCREEN_SIZE
        client_str += "\n\tName: " + self.name
        client_str += "\n\tRecurrency: " + self.recurrency
        client_str += "\n\tProbabilities: " + str(self.categories_probability)
        client_str += "\n\tTotal purchases: " + str(self.purchases_number)
        client_str += "\n\tFavorite Category: " + str(self.favorite_category)

        # Print the rest of categories from most probability to bottom
        for i in range(0, N_CATEGORIES):
            client_str += "\n\tGet probability for this category"

        return client_str

    def get_recurrency_num(self, key, recurrency_dict):
        if key in recurrency_dict:
            return recurrency_dict[key]
        else:
            return 0

    def set_random_recurrency(self):
        self.recurrency = random.choice(CLIENT_RECURRENCY_FACTOR.keys())

    def set_random_purchases_number(self, recurrency_key):
        random_purchases_num = randint(1, MAX_BOUGHT_PRODUCTS-1)
        increase_purchases_by_factor = self.get_recurrency_num(
            recurrency_key, CLIENT_RECURRENCY_FACTOR)

        total_purchases = random_purchases_num * increase_purchases_by_factor

        if total_purchases >= MAX_BOUGHT_PRODUCTS:
            total_purchases = MAX_BOUGHT_PRODUCTS

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
        categories_probability = [0] * N_CATEGORIES

        for i in range(0, N_CATEGORIES):
            categories_probability[i] = BASE_PROBABILITY

        if favourite_category in categories:
            # When Client index is valid, add extra value to that category
            top_cat_index = categories[favourite_category]
            total += TOP_PROBABILITY
            categories_probability[top_cat_index] += TOP_PROBABILITY

        # Converting values into probabilities
        for i in range(0, N_CATEGORIES):
            categories_probability[i] /= float(total)

        self.categories_probability = categories_probability
        # return products

    def generate_random_information(self, recurrency_key, favourite_category):

        self.set_random_recurrency()

        self.set_random_purchases_number(
            recurrency_key)

        self.set_random_categories_probability(
            favourite_category,
            AVAILABLE_CATEGORIES)

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

    p2 = Client('Jorge', 'medium', 'love')
    p2.generate_information()
    info = p2.to_str()

    print info
