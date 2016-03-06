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

    def test_client_purchased_volume_converts_str_to_int(self):
        purchased_volume = {
            'low': 1,
            'medium': 2,
            'high': 3
        }
        key = 'high'
        v = self.c.get_purchased_volume_num(key, purchased_volume)
        self.assertEqual(v, 3)

    def test_client_purchased_volume_returns_cero_key_not_found_or_valid(self):
        purchased_volume = {
            'low': 1
        }
        not_valid_keys = (None, 3300030303033030, 'yes')
        for key in not_valid_keys:
            vol_num = self.c.get_purchased_volume_num(key, purchased_volume)
            self.assertEqual(vol_num, 0)

    def test_client_generate_correct_number_of_purchases(self):
        c_type = 'low'
        c = Client(c_type)


if __name__ == '__main__':
    unittest.main()
