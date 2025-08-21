from django.db import models
from product.models import Product
from user.models import User
# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    