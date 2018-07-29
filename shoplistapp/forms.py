from django import forms
from .models import Shoplistclass

class ListForm(forms.ModelForm):
    class Meta:
        model = Shoplistclass
        fields = ('item','urgency', 'shop', 'quantity', 'category',)