from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
        
    def update(self, price=None, quantity=None):
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        self.save()
    
    def __str__(self):
        return f'(Product: {self.name}, price: {self.price}, quantity: {self.quantity})'