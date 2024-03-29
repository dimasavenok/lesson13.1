class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

        Category.total_categories += 1

class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Category.total_unique_products += 1
