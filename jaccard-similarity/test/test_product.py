#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app.Product import Product


class TestProductClass(unittest.TestCase):

    def setUp(self):
        name = 'Ranflax'
        _type = 'love'
        self.p = Product(name, _type)

    def test_get_product_name_after_create_product(self):
        info = ('Ranflax', 'love')
        p1 = Product(info[0], info[1])
        p1_name = p1.get_name()

        self.assertEqual('Ranflax', p1_name)

    def test_get_product_type(self):
        info = ('Name', 'love')
        p1 = Product(info[0], info[1])
        p1_type = p1.get_type()

        self.assertEqual('love', p1_type)
 
