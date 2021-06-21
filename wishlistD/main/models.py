from django.db import models

# Create your models here.

class WishList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10000, decimal_places=2)

    def __str__(self):
        return self.item_name

