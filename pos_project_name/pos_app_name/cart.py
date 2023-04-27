
class Cart:
    """
    Class for the shopping cart.
    """

    def __init__(self):
        self.items = []
        self.observers = []
        
    def add_product(self, item):
        """
        Add an item to the cart.
        """
        self.items.append(item)
        self.notify_observers(item)
        print(f"{item.get_name()} added to cart")

    def remove_item(self, item):
        """
        Remove an item from the cart.
        """
        self.items.remove(item)

    def get_products(self):
        """
        Get the list of items in the cart.
        """
        return self.items

    def attach(self, observer):
        """
        Register an observer to the cart.
        """
        self.observers.append(observer)

    def detach(self, observer):
        """
        Unregister an observer from the cart.
        """
        self.observers.remove(observer)

    def notify_observers(self, item):
        """
        Notify all registered observers when a new item is added to the cart.
        """
        for observer in self.observers:
            observer.update(item)
