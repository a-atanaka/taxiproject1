from django import forms 
from .models import TaxiModel

class PostForm(forms.ModelForm):
    class Meta():
        model = TaxiModel
        fields = (
            'myinteger',
            'regist_date',
            'priority',
        )