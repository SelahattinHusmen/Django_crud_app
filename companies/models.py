from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=200,null=True)
    
    def __str__(self): 
        return self.name

class Companies(models.Model):
    turu =(
        ("Şahıs", "Şahıs"),
        ("Büyük işletme", "Büyük işletme"),
        ("KOBİ", "KOBİ"),
        ("STK", "STK"),
    )
    Kurulus_adi = models.CharField(max_length=200,null=True)
    Kurulus_logo = models.ImageField(max_length=200,null=True,blank=True)
    Kurulus_turu = models.CharField(max_length=200,null=True, choices=turu)
    Ulke = CountryField(null=True)
    Firma_website = models.URLField(max_length=200,null=True)
    Calisan_sayisi = models.IntegerField(null=True)

    def __str__(self): 
        return self.Kurulus_adi


#class Added_companies(models.Model):
    #user = models.CharField(max_length=200,null=True)
    #companies = models.CharField(max_length=200,null=True)