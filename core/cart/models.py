from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class CartModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   

class CartItemModel(models.Model):
    cart=models.ForeignKey(CartModel,on_delete=models.CASCADE)
    product=models.ForeignKey('shop.Product',on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
    