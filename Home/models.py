from django.db import models

# Create your models here.
class Product(models.Model):
    GRADE_CHOICES = (
        ('A',"Higher Quality"),
        ('B',"Good Quality"),
        ('C',"Lower Quality"),
        
    )
    name = models.CharField(max_length=100)
    type_of_product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(max_length=100)
    grade = models.CharField(max_length=1,choices=GRADE_CHOICES)
    seasonality = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "products_images/")

    def __str__(self):
        return self.name

# class Graph(models.Model):
#     dates = models.DateField()
#     price = models.DecimalField(max_digits=4,decimal_places=2)

#     def __str__(self):
#         return f"{self.dates} - {self.price}"