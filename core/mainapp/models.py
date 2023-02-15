from django.db import models
from pathlib import Path
from time import time


def products_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return "product_{0}/avatars/{1}".format(instance.name, f"pic_{num}{suff}")


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.data_type}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=products_avatars_path)
    attributes = models.ManyToManyField(ProductAttribute, blank=True)

    def __str__(self):
        return self.name


