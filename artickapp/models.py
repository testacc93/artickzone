from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Product(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    description = models.TextField(default="This is an awesomeproduct")
    image = models.ImageField(storage=S3Boto3Storage(), default=None)
    altname = models.CharField(max_length=100, default='image')


    def __str__(self):
        return self.name
