from django.db import models

# Create your models here.

class MyApi(models.Model):
    fullname = models.CharField( max_length=50)
    code = models.CharField( max_length=50)
    mobile = models.CharField( max_length=50)