from shop.models import (Product,ProductStatus)
from decimal import Decimal
from cart.models import(CartItemModel,CartModel)

class CartSession:

    def __init__(self, session):
        self.session = session
        self._cart = self.session.get(
            "cart", {"items": [], "total_price": 0, "total_items": 0}
        )
        self.session["cart"] = self._cart

    def get_cart_items(self):
        """get all items in cart"""
        cart_items = []

        for item in self._cart["items"]:
            product = Product.objects.get(id=item["product_id"])
            cart_items.append(
                {
                    "product_id": item["product_id"],
                    "quantity": item["quantity"],
                    "product_name": product.title,
                    "total_price": product.get_price() * int(item["quantity"]),
                    "product_image": product.image.url,
                    "product_obj": product,
                }
            )

        return cart_items

    def get_total_price(self):
        """get total price of all items in cart"""
        total_price = 0
        for item in self._cart["items"]:
            product = Product.objects.get(id=item["product_id"])
            total_price += product.get_price() * int(item["quantity"])
        return total_price

    def get_quntity(self):
        """quntity for all items in cart"""
        quntity = 0
        for item in self._cart["items"]:
            quntity += int(item["quantity"])
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
        product = Product.objects.get(id=product_id)
        product_price = product.get_price()

        for item in self._cart["items"]:
            if item["product_id"] == product_id:
                item["quantity"] += 1
                break
        else:
            self._cart["items"].append({"product_id": product_id, "quantity": 1})

        self._cart["total_items"] += 1
        self._cart["total_price"] += float(product_price)
        self.save()

    def update_product(self, product_id, quantity):
        """update product quantity in cart"""
        for item in self._cart["items"]:
            if item["product_id"] == product_id:
                item["quantity"] = int(quantity)
                break
        else:
            return
        self.save()

    def remove_product(self, product_id):
        
        for item in self._cart["items"]:
            if item["product_id"] == product_id:
                self._cart["items"].remove(item)

        self.save()

    def sync_cart_from_db(self, user):
        """Sync cart items from the database to the session cart."""
        cart, created = CartModel.objects.get_or_create(user=user)
        cart_items = CartItemModel.objects.filter(cart=cart)
        
        # Create a set of product IDs already in session cart
        session_product_ids = {item['product_id'] for item in self._cart["items"]}
        
        for cart_item in cart_items:
            product_id = str(cart_item.product.id)
            if product_id in session_product_ids:
                # Update quantity for existing items
                for item in self._cart["items"]:
                    if item['product_id'] == product_id:
                        item['quantity'] = cart_item.quantity
                        break
            else:
                # Add new items from DB to session
                new_item = {
                    'product_id': product_id,
                    'quantity': cart_item.quantity
                }
                self._cart['items'].append(new_item)
        
        self.save()
        self.merge_cart_from_session_to_db(user)
    def merge_cart_from_session_to_db(self,user):
        """Merge cart items from the session cart to the database."""
        cart,created=CartModel.objects.get_or_create(user=user)

        for item in self._cart['items']:
            product_obj=Product.objects.get(id=item['product_id'],status=ProductStatus.publish.value)
            cart_item,created=CartItemModel.objects.get_or_create(cart=cart,product=product_obj)
            cart_item.quantity=item['quantity']
            cart_item.save()
        session_product_ids=[item['product_id'] for item in self._cart['items']]
        CartItemModel.objects.filter(cart=cart).exclude(product_id__in=session_product_ids).delete()



