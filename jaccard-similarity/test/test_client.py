import unittest
import numpy as np
from app.client import Client


class Client_tests(unittest.TestCase):

    def setUp(self):
        self.c = Client()

    def test_client_buy_products_top_category_is_the_maximum(self):
        top_category = 2
        products = self.c.buy_products(top_category)
        max_category = np.argmax(products)

        self.assertEqual(max_category, top_category)

    def test_client_buy_products_all_same_values_when_not_valid_index(self):

        indexes_not_valid = (-1, None, "fskdfjsdlfjsd")

        for index in indexes_not_valid:
            top_category = index
            products = self.c.buy_products(top_category)
            products_min = min(products)
            products_max = max(products)
            self.assertEqual(products_min, products_max)

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

if __name__ == '__main__':
    unittest.main()
