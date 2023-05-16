from django import forms

from .models import Item


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'description', 'price', 'image',)

        widgets = {

            'category': forms.Select(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Category',
            'default_value': 'Select',
            }),

            'name': forms.TextInput(attrs={
            'placeholder': 'Product Name',
            'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
            }),
            
            'price': forms.TextInput(attrs={
            'placeholder': 'Product Price',
            'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
            'class': 'w-1/10 rounded-xl border'
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
            'placeholder': 'Product Name',
            'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
            }),
            
            'price': forms.TextInput(attrs={
            'placeholder': 'Product Price',
            'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
            'class': 'w-1/10 rounded-xl border'
            }),
        }