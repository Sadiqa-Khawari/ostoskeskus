from django import forms
from .models import Kortti



class Korttilomake(forms.ModelForm):
    class Meta:
        model = Kortti
        fields = '__all__'
