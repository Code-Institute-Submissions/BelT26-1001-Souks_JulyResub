from django.db import models
from map.models import City


# Create your models here.
class Category(models.Model):
    """A model to represent the categories that the products will be
    divided into"""

    class Meta:
        """returns the correct plural spelling in the admin panel"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200, blank=False, null=False)
    location = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(default='')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):
    """A model to represent each of the products sold"""
    name = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size_selection = models.BooleanField(default=False, null=True, blank=True)
    colour_selection = models.BooleanField(default=False, null=True,
                                           blank=True)
    maker = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.SET_NULL)
    product_type = models.CharField(max_length=200, blank=True, null=True)
    composition = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
