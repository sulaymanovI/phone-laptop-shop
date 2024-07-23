from typing import Iterable
from django.db import models
from apps.accounts.models import User

class UploadImagePhone(models.Model):

    file=models.FileField(upload_to="product_images_phone/" )

class Phone(models.Model):

    BRAND_TYPE=(
        ("Apple", "Apple"),
        ("Samsung" , "Samsung"),
        ("Redmi" , "Redmi"),
        ("Mi" , "Mi"),
        ("LG" , "LG"),
        ("Realme" , "Realme"),
        ("Other..." , "Other...")
    )

    brand=models.CharField(choices=BRAND_TYPE,max_length=155,default="Other...")
    name=models.CharField(max_length=155 , verbose_name="Modeli" )
    price=models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name="Narxi($)")
    image=models.ManyToManyField(UploadImagePhone)
    memory=models.IntegerField(verbose_name="Xotirasi(GB)", default=0)
    release_date=models.DateField(blank=True , null=True)
    posted_ad=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True )
    seller=models.ForeignKey(to=User , on_delete=models.CASCADE , verbose_name="Sotuvchi")
    
    def __str__(self) -> str:

        return f"{self.seller.fullname if self.seller.fullname else self.seller.email}'s {self.name}"
    
 
class UploadImageLaptop(models.Model):

    file=models.FileField(upload_to="product_images_laptop/" )


class Laptop(models.Model):

    PROCESSORS=(
        ("Core i3" , "Core i3"),
        ("Core i5" , "Core i5" ), 
        ("Core i7" , "Core i7"),
        ("Ryzen 5" , "Ryzen 5"),
        ("Ryzen 7" , "Ryzen 7"),
        ("M1" , "M1"),
        ("M2" , "M2"),
        ("M3" , "M3"),
        ("Other..." , "Other...")
    )

    STORAGE_TYPES =(
        ("SSD" , "SSD"),
        ("HDD" , "HDD")
    )

    BRAND_TYPE=(
        ("Apple" , "Apple"),
        ("Asus" , "Asus"),
        ("Lenovo" , "Lenovo"),
        ("Acer" , "Acer"),
        ("HP" , "HP"),
        ("Other..." , "Other...")
    )

    brand=models.CharField(max_length=155, choices=BRAND_TYPE, default="Other...")
    name=models.CharField(max_length=155 , verbose_name="Modeli")
    price=models.DecimalField(max_digits=10 , decimal_places=2 , verbose_name="Narxi($)")
    image=models.ManyToManyField(UploadImageLaptop)
    memory=models.IntegerField(verbose_name="Xotirasi(GB)", default=0)
    processor=models.CharField(choices=PROCESSORS,max_length=155,default="Other..." , verbose_name="Protsessor turi")
    storage_type=models.CharField(choices=STORAGE_TYPES,default="SSD" ,max_length=155, verbose_name="Saqlash turi")
    release_date=models.DateField(blank=True , null=True)
    posted_ad=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True )
    seller=models.ForeignKey(to=User , on_delete=models.CASCADE , verbose_name="Sotuvchi")
    
    def __str__(self) -> str:

        return f"{self.seller.fullname if self.seller.fullname else self.seller.email}'s {self.name}"
