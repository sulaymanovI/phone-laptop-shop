from django.db import models
from apps.accounts.models import User
from apps.products.models import Phone , Laptop

class Order(models.Model):
    
    user=models.ForeignKey(to=User , on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
    
        return f"Order: {self.id} by {self.user.fullname}"
    

class PhoneOrder(models.Model):

    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    phone=models.ForeignKey(Phone , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.phone.seller.fullname}'s {self.phone.name} with price {self.phone.price}"


class LaptopOrder(models.Model):

    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    laptop=models.ForeignKey(Laptop , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.laptop.seller.fullname}'s {self.laptop.name} with price {self.laptop.price}"
   
