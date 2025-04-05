from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()
# Create your models here.

class ProductStatus(models.IntegerChoices):
    publish=1,_('متتشرشده')
    draft=2,_('در انتضار')

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #category=
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='products/',default='images/product.png')
    description=models.TextField()
    stock=models.PositiveIntegerField(default=0)
    status=models.IntegerField(choices=ProductStatus.choices,default=ProductStatus.draft.value)