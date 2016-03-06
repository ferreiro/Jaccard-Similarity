# -*- coding: utf-8 -*-

N_CATEGORIES = 5
BASE_PROBABILITY = 10
TOP_PROBABILITY = 30

# Constant factor used for calculating
# the total number of purchased one client has done
CLIENT_TYPE = {
    'low': 1,
    'medium': 2,
    'high': 3
}


class Client(object):

    def __init__(self, name='', _type='low'):
        self.name = 2
        self.products = 0
        self._type = _type

    # METHODS
    def buy_products(self, client_top_cagegory):
        """
        Return a list containing probabilities
        that the client buy products from each category.
        When 'client_top_cagegory' is provided, we
        assign 3x more probabilities to that category
        """
        total = BASE_PROBABILITY * N_CATEGORIES
        products = [0] * N_CATEGORIES
        top_cat_index = client_top_cagegory

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

    def get_purchased_volume_num(self, key, purchased_volume_dict):
        if key in purchased_volume_dict:
            return purchased_volume_dict[key]
        else:
            return 0
