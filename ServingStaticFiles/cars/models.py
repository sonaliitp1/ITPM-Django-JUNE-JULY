from django.db import models

# Create your models here.

class cars(models.Model):
    cid = models.IntegerField()
    cname =models.CharField(max_length=20)
    price = models.IntegerField()
    cimage = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.cname