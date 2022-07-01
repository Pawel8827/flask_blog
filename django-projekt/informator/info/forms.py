from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from .models import Naglowek, Slider
from django.forms.widgets import DateInput, TextInput, Textarea

class NaglowekForm(forms.ModelForm):
    
    class Meta:
        model = Naglowek
        fields = "__all__"


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['Nazwa', 'Text', 'Kolor', 'Plik', 'Czas_wyswietalnia','Data_wygasniecia' ]
        widgets = {
            'Data_wygasniecia': DateInput(attrs={'type':'date'}),
            'Kolor': TextInput(attrs={'type': 'color'}),
            'Text':Textarea(attrs={"class":"form-control", "rows":3})
        } 
        labels = {
            'Czas_wyswietalnia': ('Czas wyświetlania'),
            'Data_wygasniecia': ('Data wygaśniecia'),
        }