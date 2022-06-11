from distutils.command import upload
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Dergi(models.Model):
    kapak = models.ImageField(upload_to = "dergi")
    icerik = models.FileField(upload_to="dosya2/")
    baslik = models.CharField(max_length=50,null=False,default="")

    
    def __str__(self):
        return f"{self.baslik}"




class Yazar(models.Model):
    isim = models.CharField(max_length=50, null=False ,)
    unvan = models.CharField(max_length=50, null=False, default="")
    image = models.ImageField(upload_to ="yazar")
    hesap = models.CharField(max_length=100, null=False)
    mail = models.CharField(max_length=80,null=False,default="")

    def __str__(self):
        return f"{self.isim}"
    

class KullaniciMesaj(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=60)
    mail = models.CharField(max_length=50)
    yazi = models.CharField(max_length=100,null=False, default="")
   
   
def __str__(self):
       return self.isim









