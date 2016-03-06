#!/usr/bin/env python
# -*- coding: utf-8 -*-

LINES = 40


class Product(object):

    def __init__(self, name, product_type=""):
        self.name = name
        self.product_type = product_type

    # GETTERS
    def get_name(self):
        return self.name

    def get_type(self):
        return self.product_type

    # METHODS

    def to_str(self):
        product_str = "\n"
        product_str += "\tProduct info: " + ("-" * LINES)
        product_str += "\n\tName: " + str(self.name)
        product_str += "\n\tProduct type: " + str(self.product_type)

        return product_str


# p1 = Product('Cuchilla', 'film')
# info = p1.to_str()
# print info
