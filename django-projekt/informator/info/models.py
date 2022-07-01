
from django.db import models
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.urls import reverse



wielkosc = [
        ('XL', 'Bardzo Duży'),
        ('L', 'Duży'),
        ('M', "Średni"),
        ('S', 'Mały'),
        ('XS','Bardzo Mały')
    ]
class Naglowek(models.Model):
    
    Nazwa = models.CharField(max_length=200, default="domyślny")
    dzielnica = RichTextField()
    Kolor = ColorField( default='#FFFFFF')
    logo = models.ImageField(storage=FileSystemStorage(location='info/static/img/logo'), null=True)
    unike = models.BooleanField(default=False,)
    wielkosc= models.CharField(
        max_length=20,
        choices=wielkosc,
        default='XL',
    )
    def delete(self):
        self.logo.storage.delete(self.logo.name)
        super().delete()

    

    def extension_file(self):
        logo = self.logo.name
        abc = logo.split('.')
        return f'{abc[1]}'
    

    def __str__(self):
        return self.Nazwa

    def get_delete_url(self):
        return reverse('logo_list')
   
    def get_absolute_url(self):  
        return reverse('logo_detail', kwargs={'pk': self.pk})




class Slider(models.Model):
    Nazwa = models.CharField(max_length=200)
    Plik = models.FileField(storage=FileSystemStorage(location='info/static/move'), null=True,blank=True)
    Text = RichTextField(blank=True, null=True)
    Kolor = ColorField( default='#FFFFFF')
    Czas_wyswietalnia =models.IntegerField(default=5)
    Data_wygasniecia = models.DateField(auto_now_add=False,  null=True, auto_now=False, blank=True )
    Data_Utworzenia = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def delete(self):
        self.Plik.storage.delete(self.Plik.name)
        super().delete()
        
    def extension_file(self):
        plik = self.Plik.name
        plik_ex = plik.split('.')
        return f'{plik_ex[1]}'

    

    def __str__(self):
        return self.Nazwa   

    def get_absolute_url(self):  
        return f'/info'
    