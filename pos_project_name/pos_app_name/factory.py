


from .models import TV, Smartphone, Speakers
from .cart import Cart
from .salesperson import Salesperson

class ProductCatalog:
    """
    Singleton class for the product catalog.
    """

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.catalog = []
        self.create_catalog()

    def create_catalog(self):
        """
        Create a list of available products in the catalog.
        """
        tv = TV()
        smartphone = Smartphone()
        speakers = Speakers()
        self.catalog = [tv, smartphone, speakers]

class ProductFactory:
    """
    Factory class to create products.
    """

    def __init__(self):
        self.catalog = ProductCatalog().catalog
        self.cart = Cart()
        self.salesperson = Salesperson(self.cart)

    def create_product(self, product_type, decorators=None):
        for product in self.catalog:
            if product.get_name() == product_type:
                if decorators:
                    for decorator in decorators:
                        product = decorator(product)
                return product
        raise ValueError(f"Invalid product type: {product_type}")




# from .models import TV, Smartphone, Speakers

# class ProductCatalog:
#     """
#     Singleton class for the product catalog.
#     """

#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self):
#         self.catalog = []
#         self.create_catalog()

#     def create_catalog(self):
#         """
#         Create a list of available products in the catalog.
#         """
#         tv = TV()
#         smartphone = Smartphone()
#         speakers = Speakers()
#         self.catalog = [tv, smartphone, speakers]

# class ProductFactory:
#     """
#     Factory class to create products.
#     """

#     def __init__(self):
#         self.catalog = ProductCatalog().catalog

#     def create_product(self, product_type, decorators=None):
#         for product in self.catalog:
#             if product.get_name() == product_type:
#                 if decorators:
#                     for decorator in decorators:
#                         product = decorator(product)
#                 return product
#         raise ValueError(f"Invalid product type: {product_type}")
