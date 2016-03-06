import unittest
import numpy as np
from app.Client import Client


class Client_tests(unittest.TestCase):

    def setUp(self):
        self.c = Client()

    def test_client_categories_probability_set_after_calling_function(self):
        c1 = Client()

        favourite_category = 'love'
        categories = {
            "film": 0,
            "love": 1,
            "cooking": 2
        }

        previous_categories = c1.get_categories_probability()
        c1.set_random_categories_probability(favourite_category, categories)
        after_categories = c1.get_categories_probability()

        self.assertNotEqual(previous_categories, after_categories)

    def test_client_favorite_category_is_the_maximum_probability(self):
        c1 = Client()

        categories = {
            "film": 0,
            "love": 1,
            "cooking": 2,
            "boxing": 4
        }

        fav_category_key = 'cooking'
        fav_category_index = categories[fav_category_key]

        c1.set_random_categories_probability(fav_category_key, categories)

        categories_probability = c1.get_categories_probability()
        max_category_index = np.argmax(categories_probability)

        self.assertEqual(fav_category_index, max_category_index)

    def test_client_all_categories_same_probability_when_not_valid_cat(self):
        c1 = Client()

        categories = {
            "film": 0,
            "love": 1,
            "cooking": 2,
            "boxing": 4
        }

        wrong_keys = ('asbsabs', 2323)

        # When the key is not valid. We assign to all the categories
        # the same probability
        for key in wrong_keys:
            c1.set_random_categories_probability(key, categories)
            categories_probability = c1.get_categories_probability()
            min_probability_value = min(categories_probability)
            max_probability_value = min(categories_probability)
            self.assertEqual(min_probability_value, max_probability_value)

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
