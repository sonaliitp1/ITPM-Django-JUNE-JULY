from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=20)
    category =models.TextField(max_length=25)
    stock = models.IntegerField(max_length=2)

