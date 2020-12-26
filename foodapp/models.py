from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    category_name = models.CharField(primary_key=True, unique=True, max_length=20)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(primary_key=True, unique=True, max_length=20)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class PurchaseList(models.Model):
    purchase_id = models.AutoField(primary_key=True, unique=True)
    purchase_date = models.DateField(default=date.today, validators=[MaxValueValidator(date.today)])

class PurchaseDetail(models.Model):
    detail_id = models.AutoField(primary_key=True, unique=True)
    purchase = models.ForeignKey(PurchaseList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_cost = models.FloatField(default=0, validators=[MinValueValidator(0)])