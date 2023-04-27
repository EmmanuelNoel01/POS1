
class Salesperson:
    """
    Observer class for the salesperson.
    """

    def __init__(self, cart):
        self.cart = cart

    def update(self, product):
        self.cart.add_product(product)
        print(f"Salesperson notified: Product {product.get_name()} added to the cart")
