from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField()
    stock = models.PositiveBigIntegerField()
    description = models.TextField()