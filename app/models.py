from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='category',null=True)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='product', null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''


    def __str__(self):
        return self.name

class Inside_Products_File(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250, null=True)
    file = models.FileField(upload_to='files',null=True)
    video_file = models.FileField(upload_to='videos',null=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def fileURL(self):
        try:
            return self.file.url
        except:
            return ''



