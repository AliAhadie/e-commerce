from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

User = get_user_model()
# Create your models here.

class ProductStatus(models.IntegerChoices):
    publish=1,_('متتشرشده')
    draft=2,_('در انتضار')

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField("ProductCategory")
    title=models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True)
    image=models.ImageField(upload_to='products/',default='images/product.png')
    description=models.TextField()
    stock=models.PositiveIntegerField(default=0)
    status=models.IntegerField(choices=ProductStatus.choices,default=ProductStatus.draft.value)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    discount_percnete=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_price(self):
        if self.discount_percnete:
            return self.price - (self.price * Decimal(self.discount_percnete) / 100)
        return self.price
class ProductCategory(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True,allow_unicode=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    file=models.ImageField(upload_to='products/images')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)