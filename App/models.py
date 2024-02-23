from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_id = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.cat_name
    
class Product(models.Model):
    cat_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    pname = models.CharField(max_length=100)
    pid = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    def __str__(self) -> str:
        return self.pname
