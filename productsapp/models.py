from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class ProductModel(models.Model):
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    phone_model = models.CharField(max_length=25)
    at_date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=12)
    photo_image = models.ImageField(upload_to='media')

    def __str__(self) -> str:
        return self.name

