from .models import Product
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "assignment"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "assignment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
        }
