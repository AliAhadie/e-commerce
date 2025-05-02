from shop.models import Product
from decimal import Decimal


class CartSession:
    """ """

    def __init__(self, session):
        self.session = session
        self._cart = self.session.get(
            "cart", {"items": [], "total_price": 0, "total_items": 0}
        )
        self.session["cart"] = self._cart

    def get_cart_items(self):
        """get all items in cart"""
        cart_items = self._cart["items"]
        for item in cart_items:
            product = Product.objects.get(id=item["product_id"])
            item['product_name']= product.title
            item['total_price'] = product.get_price() * item["quantity"]
            item['product_image'] = product.image.url
            

        return cart_items    


    def get_total_price(self):
        """get total price of all items in cart"""
        total_price = 0
        for item in self._cart["items"]:
            product = Product.objects.get(id=item["product_id"])
            total_price += product.get_price() * item["quantity"]
        return total_price

    def get_quntity(self):
        """quntity for all items in cart"""
        quntity = 0
        for item in self._cart["items"]:
            quntity += item["quantity"]
        return quntity

    def save(self):
        """save session data"""
        self.session.modified = True

    def clear(self):
        """delete session data"""
        self._cart["items"] = []
        self._cart["total_price"] = 0
        self._cart["total_items"] = 0
        self.save()

    def add_product(self, product_id):
        """add product to cart"""
        for item in self._cart["items"]:
            if item["product_id"] == product_id:
                item["quantity"] += 1
                break
        else:
            self._cart["items"].append({"product_id": product_id, "quantity": 1})
        self._cart["total_items"] += 1
        self._cart["total_price"] += 1
