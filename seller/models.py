from django.db import models

#this app is to manage selled products in snackbar

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # quantity = models.IntegerField()

    def __str__(self):
        return self.name
#model for product selling
class Sell(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_sold = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity}- {self.Product.name}----{self.Product.price * self.quantity}'
#model for expence tracking
class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} spent {self.amount} on {self.date}'