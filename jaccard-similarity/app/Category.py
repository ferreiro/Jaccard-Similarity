CATEGORIES = {
    "film": 0,
    "love": 1,
    "cooking": 2
}


"""
Singlenton Class
"""
class Category(object):

    def get_categories(self):
        return CATEGORIES

    def get_category_number(self, category_str):
        if category_str in CATEGORIES:
            return CATEGORIES[category_str]
        else:
            return -1
