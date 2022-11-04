from django.db import models

# Create your models here.


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, unique=False)
    note = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=1)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name
