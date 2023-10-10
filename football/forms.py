from django import forms
from .models import FieldModel


class FieldForm(forms.ModelForm):
    name_uz=forms.CharField()
    name_en=forms.CharField()
    name_ru=forms.CharField()

    
    description_uz=forms.CharField()
    description_en=forms.CharField()
    description_ru=forms.CharField()


    address_uz=forms.CharField()
    address_en=forms.CharField()
    address_ru=forms.CharField()

    class Meta:
        model=FieldModel
        exclude=('name', 'description','address' )