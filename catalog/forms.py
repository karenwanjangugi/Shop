from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "w-full px-4 py-3 bg-gray-100 rounded-lg border-2 border-gray-200 focus:ring-4 focus:ring-blue-300 focus:border-blue-500 transition duration-300"}
            ),
            "description": forms.Textarea(
                attrs={"class": "w-full px-4 py-3 bg-gray-100 rounded-lg border-2 border-gray-200 focus:ring-4 focus:ring-blue-300 focus:border-blue-500 transition duration-300", "rows": 4}
            ),
            "price": forms.NumberInput(
                attrs={"class": "w-full px-4 py-3 bg-gray-100 rounded-lg border-2 border-gray-200 focus:ring-4 focus:ring-blue-300 focus:border-blue-500 transition duration-300"}
            ),
            "stock": forms.NumberInput(
                attrs={"class": "w-full px-4 py-3 bg-gray-100 rounded-lg border-2 border-gray-200 focus:ring-4 focus:ring-blue-300 focus:border-blue-500 transition duration-300"}
            ),
        }
        