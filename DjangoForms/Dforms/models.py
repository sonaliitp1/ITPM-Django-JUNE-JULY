from django.db import models

# Create your models here.
class Dforms(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(default="Admin",max_length=10)

    def __str__(self):
        return self.username
    




