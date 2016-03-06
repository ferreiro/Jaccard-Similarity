import unittest
import numpy as np
from app.client import Client


class Client_tests(unittest.TestCase):

    def setUp(self):
        self.c = Client()

    def test_client_top_category_is_the_maximum_probability(self):
        categories = {
            "film": 0,
            "love": 1,
            "cooking": 2
        }
        client_fav_category = 'cooking'
        category_index = 2

        categories_probability = self.c.set_random_categories_probability(
            client_fav_category, categories)

        max_category_index = np.argmax(categories_probability)
        self.assertEqual(category_index, max_category_index)

    def test_client_all_categories_has_same_value_when_favorite_not_valid(self):
        categories = {
            "film": 0,
            "love": 1,
            "cooking": 2
        }
        client_fav_category = 'sdflkasjdlfkjsdlkfjsadlfkjasdlkfjsd'

        categories_probability = self.c.set_random_categories_probability(
            client_fav_category, categories)

        cats_min = min(categories_probability)
        cats_max = max(categories_probability)

        self.assertEqual(cats_min, cats_max)

    # def test_client_categories_probability_all_same_values_when_not_valid_index(self):
    #
    #     indexes_not_valid = (-1, None, "fskdfjsdlfjsd")
    #
    #     for index in indexes_not_valid:
    #         top_category = index
    #         products = self.c.set_products_probability(top_category)
    #         products_min = min(products)
    #         products_max = max(products)
    #         self.assertEqual(products_min, products_max)

    def test_client_recurrency_converts_str_to_int(self):
        recurrency = {
            'low': 1,
            'medium': 2,
            'high': 3
        }
        key = 'high'
        v = self.c.get_recurrency_num(key, recurrency)
        self.assertEqual(v, 3)

    def test_client_recurrency_returns_cero_when_key_not_found_or_valid(self):
        recurrency = {
            'low': 1
        }
        not_valid_keys = (None, 3300030303033030, 'yes')
        for key in not_valid_keys:
            vol_num = self.c.get_recurrency_num(key, recurrency)
            self.assertEqual(vol_num, 0)
    #
    # def test_client_returns_false_when_not_valid_recurrency_name(self):
    #     wrong_recurrencies = ('fdsfsdfd', 'highhigh', 34343, None)
    #     valid_recurrency_dict = {
    #         'low': 1,
    #         'medium': 2,
    #         'high': 3
    #     }
    #
    #     for value in wrong_recurrencies:
    #         valid = self.c.is_valid_recurrency(value, valid_recurrency_dict)
    #         self.assertEqual(valid, False)

    def test_client_number_of_products_updated_when_valid_recurrency(self):
        recurrency_key = 'high'
        previous_purchases_number = self.c.get_purchases_number()
        self.c.set_random_purchases_number(recurrency_key)
        after_purchases_number = self.c.get_purchases_number()

        self.assertNotEqual(previous_purchases_number, after_purchases_number)

    def test_client_number_of_products_are_0_when_wrong_recurrency(self):
        recurrency_key = 'sdfsdlfjhsdkjghdfkgjhdfskjghds'
        previous_purchases_number = self.c.get_purchases_number()
        self.c.set_random_purchases_number(recurrency_key)
        after_purchases_number = self.c.get_purchases_number()

        self.assertEqual(previous_purchases_number, after_purchases_number)

    def test_client_generate_random_information_correctly(self):
        # TODO: make a test to check that this function calls
        # - set_random_purchases_number
        # - categories_probability
        pass


if __name__ == '__main__':
    unittest.main()
