
from abc import ABC, abstractmethod

class Product(ABC):
    """
    Abstract class for products.
    """

    @abstractmethod
    def get_name(self):
        pass

class TV(Product):
    """
    Concrete class for TVs.
    """

    def get_name(self):
        return "TV"

class Smartphone(Product):
    """
    Concrete class for smartphones.
    """

    def get_name(self):
        return "Smartphone"

class Speakers(Product):
    """
    Concrete class for speakers.
    """

    def get_name(self):
        return "Speakers"

class ProductDecorator(Product):
    """
    Abstract class for product decorators.
    """
    def __init__(self, product):
        self._product = product

    def get_name(self):
        return self._product.get_name()
    


class GiftWrap(ProductDecorator):
    """
    Concrete decorator for gift wrapping a product.
    """

    def __init__(self, product):
        super().__init__(product)

    def get_name(self):
        return f"Gift wrapped {self._product.get_name()}"
