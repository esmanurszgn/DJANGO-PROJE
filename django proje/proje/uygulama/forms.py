from django import forms
from django.forms import ModelForm, TextInput 
from .models import KullaniciMesaj

class KullaniciMesajForm(forms.ModelForm):
    class Meta:
        model = KullaniciMesaj
        fields = ('isim','soyisim','mail','yazi')
        widgets = {
            'isim' : TextInput(attrs={
                'class' : 'input'
            }),
             'soyisim' : TextInput(attrs={
                'class' : 'input'
            }),
             'mail' : TextInput(attrs={
                'class' : 'input'
            }),
             'yazi' : TextInput(attrs={
                'class' : 'textarea'
            }),
        }

        