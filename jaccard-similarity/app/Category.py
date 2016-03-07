from Variables import Variables

const_vars = Variables()


CATEGORIES = const_vars.CATEGORIES()

"""
Singlenton Class
"""
class Category(object):

    def __init__(self):
        self.categories = CATEGORIES
        self.N_categories = len(self.categories)

    def CATEGORIES(self):
        return self.categories

    def N_CATEGORIES(self):
        return self.N_categories

    def get_categories(self):
        return self.categories

    def get_categories_length(self):
        return self.N_categories

    def get_category_number(self, category_str):
        if category_str in self.categories:
            return self.categories[category_str]
        else:
            return -1
