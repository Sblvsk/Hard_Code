from django.db import models
from pathlib import Path
from time import time


def products_avatars_path(instance, filename):
    num = int(time() * 1000)
    suff = Path(filename).suffix
    return f"product_{instance.product}/avatars/{f'pic_{num}{suff}'}"


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


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Product(models.Model):
    objects = ProductManager

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=products_avatars_path, blank=True, null=True)
    attributes = models.ManyToManyField(ProductAttribute, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    deleted = models.BooleanField(default=False)

    def delete(self, *args):
        self.deleted = True
        self.save()
