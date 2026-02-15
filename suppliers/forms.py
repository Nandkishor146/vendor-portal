from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ('status', 'is_approved', 'created_at')
        widgets = {
            'list_of_material': forms.CheckboxSelectMultiple(),
        }    