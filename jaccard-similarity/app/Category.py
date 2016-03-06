
CATEGORIES = {
    "film": 0,
    "love": 1,
    "cooking": 2
}

"""
Singlenton Class
"""
class Category(object):

    def __init__(self):
        self.categories = CATEGORIES
        self.N_categories = len(self.categories)

    def get_categories(self):
        return self.categories

    def get_categories_length(self):
        return self.N_categories

    def get_category_number(self, category_str):
        if category_str in self.categories:
            return self.categories[category_str]
        else:
            return -1
