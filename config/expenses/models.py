from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField((), auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
